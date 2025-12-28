
# 📊 Graph-Based Analysis of Distributed System Behavior

## 📌 Project Overview

This project focuses on analyzing the behavior of a **distributed microservice system** using **graph-based modeling**.  
The goal is to understand how different services communicate, identify critical components, and analyze failure patterns using network analysis techniques.

Instead of treating system logs as raw data, they are modeled as a **graph**, where:

- **Services** are represented as **nodes**
- **Communications** between services are represented as **edges**
- **Failures** are highlighted and analyzed separately

This approach helps in understanding **system stability, reliability, and bottlenecks**, which are key concerns in distributed systems.

---

## 🎯 Objectives of the Project

The main objectives of this project are:

- To model microservice communication using **graph structures**
- To analyze **dependencies between services**
- To identify **bottlenecks and failure-prone components**
- To understand system behavior using **graph metrics**
- To demonstrate how graph analysis supports **distributed system design and reliability analysis**

## 🧠 Key Concepts (Explained Simply)

### 🔹 Distributed System

A **distributed system** is a collection of independent services that work together to perform tasks.

**Example services:**
- Frontend  
- Authentication Service  
- Database  
- Payment Service  

Each service communicates with others over a network to complete requests.

---

### 🔹 Graph-Based Modeling

A **graph** is used to represent system behavior in a structured way:

| Graph Component | Meaning |
|----------------|---------|
| Node | A service (e.g., Database, Payment) |
| Edge | Communication between services |
| Direction | Request flow |
| Edge Color | Success or failure |

This representation makes system behavior **visual, structured, and easy to analyze**.

---

### 🔹 Why Graphs?

Graphs help answer important system-level questions such as:

- Which service is most important?
- Where do failures occur?
- Which service acts as a bottleneck?
- How do failures propagate across the system?

Using graphs allows us to better understand **dependencies, reliability, and system design weaknesses**.

## 📁 Dataset Description

The dataset simulates **microservice communication logs** generated in a distributed system.

### Columns Explained

| Column | Description |
|------|-------------|
| timestamp | Time of request |
| source_service | Service making the request |
| destination_service | Service receiving the request |
| response_time | Response time in milliseconds |
| status | Success or failure |

### Example

`Frontend → Payment → failure`

This means the frontend attempted to process a payment request, but the request failed.

---

## ⚙️ Methodology

### Step 1: Data Loading
System logs are loaded using **Pandas**.

---

### Step 2: Graph Construction
- Each service is represented as a **node**
- Each request is represented as a **directed edge**
- Failure status is stored as an **edge attribute**

---

### Step 3: Visualization
- Graph is plotted using **NetworkX**
- Important nodes appear larger
- Failed connections are highlighted
- Layout is optimized for clarity and readability

---

### Step 4: Analysis
The following aspects are analyzed:
- Node importance
- Dependency structure
- Failure-prone services
- Communication patterns

---

## 📈 Graph Metrics Explained

### 🔹 Degree Centrality
Measures how connected a service is.

📌 **High value → Important service**

**Examples:**
- Frontend  
- Database  

---

### 🔹 In-Degree
Shows how many services depend on a service.

📌 **High in-degree → Bottleneck**

**Example:**
- Database

---

### 🔹 Out-Degree
Shows how many services a component calls.

📌 **High out-degree → Coordinator service**

**Example:**
- Frontend

---

### 🔹 Failure Analysis
Tracks which services experience failures.

📌 **Findings:**
- Payment service has a higher failure rate
- Failures propagate to dependent services

---

## 📊 Key Observations

✔ Frontend acts as a central control point  
✔ Database is a major dependency  
✔ Payment service is failure-prone  
✔ System exhibits centralized architecture  
✔ Failures can propagate across services  

---

## 🧠 Interpretation

This analysis shows that:

- Centralized services increase system risk  
- Failures in one service can affect multiple components  
- Graph-based modeling helps identify weak points  
- The system lacks strong fault isolation  

Such insights are critical for:
- Improving system reliability  
- Designing fault-tolerant architectures  
- Optimizing service dependencies  

---

## 🖼️ Visualization Output

The system graph is saved at:

`visuals/system_graph.png`


It visually represents:
- Service dependencies  
- Communication flow  
- Failure locations  

---

## 🧪 Technologies Used

- Python  
- Pandas  
- NetworkX  
- Matplotlib

#### This project demonstrates:

- Practical distributed systems analysis

- Application of graph theory

- System behavior modeling

- Data-driven reasoning

- Research-oriented problem solving
