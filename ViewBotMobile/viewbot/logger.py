class Logger:
    def __init__(self, max_lines=50):
        self.logs = []
        self.max_lines = max_lines
    
    def add_log(self, message):
        """Add a log message"""
        timestamp = time.strftime("%H:%M:%S")
        self.logs.append(f"[{timestamp}] {message}")
        
        # Keep only recent logs
        if len(self.logs) > self.max_lines:
            self.logs = self.logs[-self.max_lines:]
    
    def get_logs(self):
        """Get all logs as string"""
        return "\n".join(self.logs[-15:])  # Show last 15 lines
    
    def clear(self):
        """Clear all logs"""
        self.logs = []