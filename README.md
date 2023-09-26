# PyPortal Titano

Playing with the [Adafruit PyPortal Titano](https://learn.adafruit.com/adafruit-pyportal-titano) hardware.

> The **PyPortal Titano** ... is our easy-to-use IoT device that allows you to create all the things for the
> “Internet of Things” in minutes. Make custom touch screen interface GUIs, all open-source, and Python-powered using
> tinyJSON / APIs to get news, stock, weather, cat photos, and more...

## Local setup

Assumes a Windows host machine environment.

> This setup is a little funky, but it allows for staying in VS Code while having full access to the device.
> An alternate approach of cloning the repo directly into the device _works_, but editing and other file operations are slow.

In VS Code, ensure the following extensions are installed:

- [CircuitPython](https://marketplace.visualstudio.com/items?itemName=joedevivo.vscode-circuitpython).
- [Trigger Task on Save](https://marketplace.visualstudio.com/items?itemName=gruntfuggly.triggertaskonsave).
- Python, Pylance, Black, Flake8 etc. as needed

Clone the repository to a location other than the device `CIRCUITPY` directory:

```console
git clone https://github.com/thekaveman/pyportal-titano.git
```

Create a settings file from the sample:

```console
cp settings.sample.toml settings.toml
```

Open the repository in VS Code:

```console
cd pyportal-titano
code .
```

Plug the device into a USB port on the host machine, the `CIRCUITPY` directory should open in Explorer.
Note the drive letter, and update `args` in `.vscode/tasks.json` as needed.

In the new settings file, edit `WIFI_SSID` and `WIFI_PASSWORD` to a local AP for Internet access.

If the `RELOAD` setting is `True`, the device automatically reloads and reruns `main.py` when it detects file changes.

## How this works

Keeping the repository files in a separate directory from the device `CIRCUITPY` directory makes `git` and other file
operations work as expected during development time.

- device driver code (`boot.py`, `main.py`) can read application code from `/app` like a normal Python package
- the _CircuitPython extension_ keeps the on-device [`CircuitPython`](https://circuitpython.org/) version updated
- the _CircuitPython extension_ provides device-specific Pylance bindings to CircuitPython for the VS Code experience
- the _CircuitPython extension_ provides a _serial monitor_ to interact with device input/output in VS Code's terminal pane
- [CircuitPython as of 8.x uses `settings.toml`](https://docs.circuitpython.org/en/8.2.x/docs/environment.html) to store config

The _Trigger Task on Save extension_ does exactly what it says on the box, building on VS Code's `task.json` framework. The
`sync` task runs the batch script `.vscode/sync.cmd` on saves to `*.py` or `*.toml` files, copying source code onto the device.
