# StreamSim: Real-Time Data Streaming Simulator

This fork of StreamSim has been substantially modified to mimic a stream of online reviews produced by yelp. It stands up a bare-bones WSGI server using Flask. Whenever that server is polled (i.e. a request is made to the relevant endpoint) it grabs a fresh batch of data and delivers it to the requestor.

In turn, the requestor performs some light-weight processing on that data, and writes it to the file. The requestor can be seen as 'ingesting' the data. This requestor effectively streams the data by appending it to a file.

Our task is to stand up this infrastructure and design a Kafka Connect connector that processes this stream in real time. Configuration is necessary to make this work properly. I will provide configuration files in real time as we progress through this exercise. 

Following this, we will set up an automatic consumer for this data, in our penultimate session. We can use Apache Spark, Apache Flink, or even Kafka Streams to this end.

In our final class we will link this stream to a real-time-updated dashboard using OpenSearch. 

StreamSim is a real-time data streaming simulator tool that allows researchers and developers to simulate real-time streaming behavior for tabular data. It provides a convenient way to test real-time applications when the actual real-time data source is not yet available or when simulating different scenarios for testing purposes.

## Table of Contents

- [Documentation](#documentation)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Documentation

For detailed instructions on how to use the functions and modules provided by StreamSim, please refer to the [StreamSim Documentation](https://usc-infolab.github.io/StreamSim/).


## Features

- Simulates real-time streaming behavior for tabular data.
- Supports stream simulation from a database table or a CSV file.
- Customizable data processing and simulation logic.
- Easy configuration.


## Prerequisites

Before using StreamSim, make sure you have the following prerequisites installed:

- Python 3.x
- Required dependencies (see Installation section)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/NIH-W4H/StreamSim.git
   ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Configure the application settings in the `conf.py` file. Specify the database connection details, dataset path, timeout interval, and other relevant parameters.

2. Implement the desired data processing logic in the `process_stream()` function in the `stream_sim.py` file. Customize it to suit your specific requirements.

3. Start the Flask server to enable stream simulation:

   ```bash
   python stream_sim.py
   ```

4. In a separate terminal, run the ingest_stream.py script to periodically fetch streams from the Flask server:
    ```bash
    python ingest_stream.py
    ```

5. Observe the simulated stream data and verify that it meets your expectations.

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](https://github.com/NIH-W4H/StreamSim/blob/main/LICENSE). Feel free to use and modify this code for your own purposes.
