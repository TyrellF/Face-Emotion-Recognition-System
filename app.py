from flask import Flask, render_template, jsonify
import subprocess
import sys
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('techhunters.html')

@app.route('/run_script')
def run_script():
    try:
        # Check if camera is available and model files exist
        if not os.path.exists('emotiondetector.h5'):
            return "Error: Model file 'emotiondetector.h5' not found. Please ensure the model is trained and saved."
        
        if not os.path.exists('emotiondetector.json'):
            return "Error: Model configuration file 'emotiondetector.json' not found."
        
        # Run the emotion detection script
        result = subprocess.check_output([sys.executable, 'run_script.py'], 
                                       stderr=subprocess.STDOUT, 
                                       timeout=300)  # 5 minute timeout
        return f"Emotion detection started successfully!\n\nOutput: {result.decode('utf-8')}"
        
    except subprocess.TimeoutExpired:
        return "Emotion detection session completed (timeout reached)"
    except subprocess.CalledProcessError as e:
        return f"Error running emotion detection: {e.output.decode('utf-8')}"
    except FileNotFoundError:
        return "Error: Python interpreter not found or script file missing"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

@app.route('/status')
def status():
    """Check if the system is ready to run emotion detection"""
    status_info = {
        'model_exists': os.path.exists('emotiondetector.h5'),
        'config_exists': os.path.exists('emotiondetector.json'),
        'script_exists': os.path.exists('run_script.py'),
        'python_available': True
    }
    
    all_ready = all(status_info.values())
    status_info['ready'] = all_ready
    
    return jsonify(status_info)

if __name__ == '__main__':
    print("Starting TECH HUNTERS Emotion Detection System...")
    print("Make sure your camera is connected and working properly.")
    app.run(debug=True, host='0.0.0.0', port=5000)
