# Hands-On Learning: Real Time Data Pipeline with Simulated Streaming

This fork of StreamSim has been substantially modified to mimic a stream of online reviews produced by [Yelp](https://business.yelp.com/external-assets/files/Yelp-JSON.zip). It stands up a bare-bones WSGI server using Flask. Whenever that server is polled (i.e. a request is made to the relevant endpoint) it grabs a fresh batch of data and delivers it to the requestor. In turn, the requestor performs some light-weight processing on that data, and writes it to the file. The requestor can be seen as 'ingesting' the data. This requestor effectively streams the data by appending it to a file.

## The Yelp Reviews Dataset

Note that we'll be using the ...reviews.json dataset. Its schema is:

 - business_id: string (nullable = true)
 - cool: long (nullable = true)
 - date: string (nullable = true)
 - funny: long (nullable = true)
 - review_id: string (nullable = true)
 - stars: double (nullable = true)
 - text: string (nullable = true)
 - useful: long (nullable = true)
 - user_id: string (nullable = true)

I recommend using a sample from this data as it is quite large and may slow you down as a result! I used Spark to read and parse the data, writing it out as a series ~20 CSV file partitions. I chose one partition at random for the in-class demonstration. 

## Our Objectives

Our task is to stand up this infrastructure and design a Kafka Connect connector that processes this stream in real time. Configuration is necessary to make this work properly. I will provide configuration files in real time as we progress through this exercise. 

Following this, we will set up an automatic consumer for this data, in our penultimate session. We can use Apache Spark, Apache Flink, or even Kafka Streams to this end.

In our final class we will link this stream to a real-time-updated dashboard using OpenSearch. 

## Setup

I am using Python version 3.12. You are free to to use this version or higher, but don't harp on this point. 

### Step 1
Clone the repository using Git.
```sh
mkdir emtech-project
cd emtech-project
git clone https://github.com/ugoetudo/StreamSimFlex.git
```
You'll see that a new directory `StreamSimFlex` has been created. 

### Step 2
Create a python virtual environment. Please do not use Anaconda (conda), it is awful. Make sure you have the latest version of pip installed. 
```sh
python -m pip install --upgrade pip
```
Ensuring that you are in the directory `emtech-project`, create a Python virtual environment (commonly called a venv) and activate it (replace my-env-name with an environment name of your choosing, keeping in mind that it is a path):
```sh
python -m venv my-env-name
# for windows:
my-env-name\Scripts\activate
# mac/wsl
./my-env-name/Scripts/activate
```
Now, install the projects main dependencies:
```sh
pip install -r StreamSimFlex/requirements.txt
```
If you get an error "cannot import name 'url_quote' from 'werkzeug.urls'...:
```sh
pip install --upgrade Flask Werkzeug Flask-Login
```

## StreamSim Documentation

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
- Required dependencies (See [Setup](#setup) section above)

## Installation

See [Setup](#setup) section above

## Usage

1. Configure the application settings in the `conf.py` file. Specify the database connection details, dataset path, timeout interval, and other relevant parameters.

2. Implement the desired data processing logic in the `process_stream()` function in the `stream_sim.py` file. Customize it to suit your specific requirements.

3. Start the Flask server to enable stream simulation:

   ```sh
   python stream_sim.py
   ```

4. In a separate terminal, run the ingest_stream.py script to periodically fetch streams from the Flask server:
    ```sh
    python ingest_stream.py
    ```

5. Observe the simulated stream data and verify that it meets your expectations.

## Contributing
Contributions are NOT welcome! If you have any suggestions, bug reports, or feature requests, please keep them to yourself (I kid... open an issue, pull request, file a bug report).

## License
This project is licensed under the [MIT License](https://github.com/NIH-W4H/StreamSim/blob/main/LICENSE). Feel free to use and modify this code for your own purposes.
