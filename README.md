# J2Live

J2Live is a web-based application that allows users to edit and render Jinja2 templates with YAML variables. It provides a user-friendly interface with Monaco Editor for editing and rendering templates in real-time.

## Features

- **YAML Editor**: Edit YAML variables.
- **Jinja2 Editor**: Edit Jinja2 templates.
- **Output Editor**: View the rendered output.
- **Theme Selection**: Switch between different themes (Everforest Dark, Nord).
- **FastAPI Integration**: Built on top of FastAPI for backend services.
- **NiceGUI Integration**: Utilizes NiceGUI for the frontend components.

## Installation

### Using Docker

1. Build the Docker image:

    ```sh
    docker build -t j2live .
    ```

2. Run the Docker container:

    ```sh
    docker run -p 8000:8000 j2live
    ```

### Locally

1. Create a virtual environment:

    ```sh
    python3 -m venv venv
    ```

2. Activate the virtual environment:

    ```sh
    source venv/bin/activate
    ```

3. Clone the repository (as so static files are accessible)

    ```sh
    git clone https://github.com/martydingo/j2live.git
    ```

4. Install J2Live:

    ```sh
    pip3 install git+https://github.com/martydingo/j2live
    ```

5. Run J2Live:

    ```sh
    python3 -m j2live
    ```

## Usage

1. Open your web browser and navigate to `http://localhost:8000`.
2. Use the YAML Editor to input your YAML variables.
3. Use the Jinja2 Editor to input your Jinja2 template.
4. The rendered output will be displayed in the Output Editor in realtime.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Authors

- Martin George ([marty@dingo.foo](mailto:marty@dingo.foo))

For more information, please refer to the [documentation](docs/README.md).
