## First, create a virtual environment to isolate the dependencies for this project. You can use `venv` or `virtualenv` to create a virtual environment.

For macOS and Linux, run the following command in your terminal:

```bash
python3 -m venv myenv
source myenv/bin/activate
python3 -m pip install -r requirements.txt
```
To deactivate the virtual environment, simply run:

```bash
deactivate
```

## Run the Project

Terminal 1 – Start the API server
```bash
python3 app.py
```

Terminal 2 – Run the scripts to test the API endpoints
```bash
python3 scripts/label_detection.py
python3 scripts/text_detection.py
python3 scripts/content_moderation.py
```