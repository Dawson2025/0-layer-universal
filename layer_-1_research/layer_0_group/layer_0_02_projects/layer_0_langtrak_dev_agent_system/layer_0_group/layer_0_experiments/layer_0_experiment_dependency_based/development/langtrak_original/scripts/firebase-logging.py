#!/usr/bin/env python3
# resource_id: "1b847e5e-3c6d-4a6d-9ccb-271c32389714"
# resource_type: "document"
# resource_name: "firebase-logging"
"""
firebase-logging.py

Centralized logging for Firebase operations.
"""

import logging
import json
from datetime import datetime
from typing import Dict, Any

class FirebaseLogger:
    def __init__(self, project_id: str):
        self.project_id = project_id
        self.logger = logging.getLogger(f"firebase-{project_id}")
        self.logger.setLevel(logging.INFO)
        
        # Create file handler
        handler = logging.FileHandler(f"logs/firebase-{project_id}.log")
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def log_operation(self, operation: str, details: Dict[str, Any]):
        """Log Firebase operations."""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "project": self.project_id,
            "operation": operation,
            "details": details
        }
        
        self.logger.info(json.dumps(log_entry))
    
    def log_error(self, operation: str, error: str):
        """Log Firebase errors."""
        self.logger.error(f"Operation: {operation}, Error: {error}")

# Usage example
if __name__ == "__main__":
    logger = FirebaseLogger("lang-trak-dev")
    logger.log_operation("configure_domains", {
        "domains": ["localhost", "127.0.0.1"],
        "success": True
    })
