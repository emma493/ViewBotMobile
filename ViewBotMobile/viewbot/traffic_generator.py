import requests
from fake_useragent import UserAgent
import time
import random
from threading import Thread, Lock

class TrafficGenerator:
    def __init__(self):
        self.ua = UserAgent()
        self.is_running = False
        self.progress = 0
        self.total_views = 0
        self.completed_views = 0
        self.lock = Lock()
    
    def generate_view(self, url, logger=None):
        """Generate a single view"""
        try:
            headers = {
                'User-Agent': self.ua.random,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            
            with self.lock:
                self.completed_views += 1
                self.progress = (self.completed_views / self.total_views) * 100
            
            if logger:
                logger.add_log(f"✓ View {self.completed_views}/{self.total_views} generated")
            
            return response.status_code == 200
        
        except Exception as e:
            if logger:
                logger.add_log(f"✗ Error: {str(e)}")
            return False
    
    def generate_mass_traffic(self, url, min_sessions, max_sessions, total_views, delay, logger=None):
        """Generate mass traffic with multiple sessions"""
        self.is_running = True
        self.total_views = total_views
        self.completed_views = 0
        self.progress = 0
        
        if logger:
            logger.add_log(f"🚀 Starting {total_views} views for {url}")
            logger.add_log(f"👥 Using {min_sessions}-{max_sessions} simultaneous sessions")
        
        threads = []
        views_per_session = total_views // max_sessions
        
        for i in range(max_sessions):
            thread = Thread(
                target=self.session_worker,
                args=(url, views_per_session, delay, logger),
                daemon=True
            )
            threads.append(thread)
            thread.start()
            time.sleep(random.uniform(0.1, 0.5))
        
        for thread in threads:
            thread.join()
        
        self.is_running = False
        if logger:
            logger.add_log("✅ Traffic generation completed!")
    
    def session_worker(self, url, views, delay, logger):
        """Worker for each session"""
        for i in range(views):
            if not self.is_running:
                break
            self.generate_view(url, logger)
            time.sleep(delay + random.uniform(-0.5, 0.5))
    
    def get_progress(self):
        """Get current progress percentage"""
        return self.progress
    
    def stop(self):
        """Stop traffic generation"""
        self.is_running = False