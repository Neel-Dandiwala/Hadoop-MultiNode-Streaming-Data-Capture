# Hadoop MultiNode Streaming Data Capture 🚀

## Project Overview

The **Hadoop-MultiNode-Streaming-Data-Capture** project is an immersive big data solution showcasing the seamless integration of diverse Hadoop frameworks. Designed to capture, process, and store streaming data, the project employs Docker and Docker Compose for an effortless multi-node setup. Key components include:

### 📡 Apache Kafka

Distributed streaming platform enabling real-time data flow across components.

### 🗄️ Apache Hadoop HDFS

Distributed file system offering scalable and reliable storage for massive datasets.

### 🦁 Apache ZooKeeper

Coordinator for distributed systems, ensuring synchronization and configuration data integrity.

### 🐘 PostgreSQL and MongoDB

Integrated databases showcasing Hadoop's versatility with various data storage systems.

### 🚀 Debezium

Facilitates change data capture from PostgreSQL to Kafka, demonstrating seamless integration.

### 🎛️ Control Center and Debezium UI

User-friendly interfaces for monitoring Kafka and Debezium connectors, enhancing manageability.

### 🩺 Health Monitoring and Random Log Generation

Custom script generates health logs at intervals, stored in HDFS, demonstrating Hadoop's data capture and processing capabilities.

## Getting Started

Follow the instructions in the Docker Compose file and configuration files to effortlessly deploy the entire environment. This project serves as both a learning resource and a practical example of streaming and batch processing integration in a multi-node setup.

## 🚧 Project Structure

```bash
project-root/
│
├── docker-compose.yml
├── connect-hdfs-sink.json
├── generate_logs.sh
├── ...
│
├── namenode/
│   ├── Dockerfile
│   └── ...
│
├── resourcemanager/
│   ├── Dockerfile
│   └── ...
│
├── historyserver/
│   ├── Dockerfile
│   └── ...
│
├── ...
```

Feel free to explore and modify the project based on your specific use cases and requirements. Happy coding! 🌐🛠️