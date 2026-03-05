#!/usr/bin/env python3
# resource_id: "2f34e20e-aec0-45fc-8768-101cfafc2858"
# resource_type: "document"
# resource_name: "test_app"

print("Starting Flask app test...")

try:
    from flask import Flask
    print("✅ Flask imported successfully")
    
    app = Flask(__name__)
    print("✅ Flask app created")
    
    @app.route('/')
    def test():
        return "Flask app is working!"
    
    print("✅ Route defined")
    
    if __name__ == '__main__':
        import os
        port = int(os.environ.get('PORT', 5000))
        print(f"✅ Starting Flask app on port {port}...")
        app.run(host='0.0.0.0', port=port, debug=True)
        
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()