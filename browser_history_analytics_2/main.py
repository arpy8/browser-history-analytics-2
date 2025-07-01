import os
import sys
import warnings
import subprocess as sb
from browser_history_analytics_2.utils import print_content, PORT

warnings.filterwarnings("ignore")

def main():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(script_dir, "app.py")
        
        if not os.path.exists(script_path):
            print(f"Error: Could not find app.py at {script_path}")
            sys.exit(1)
        
        print_content()
        
        with open(os.devnull, 'w') as fnull:
            sb.run([
                sys.executable, "-m", "streamlit", "run", script_path,
                "--server.port", str(PORT),
            ], check=True, stdout=fnull, stderr=fnull)
        

    except sb.CalledProcessError as e:
        print(f"Error running Streamlit: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()