# 📡 IoT Kafka + Spark + Delta Lake

Projeto de Engenharia de Dados que simula um pipeline em tempo real utilizando **Kafka**, **Apache Spark** e **Delta Lake**, com arquitetura baseada em camadas (_Medalhão_). A solução captura dados de sensores IoT, publica em tópicos Kafka, consome com Spark e persiste os dados tratados em formato Delta.

## 📌 Tecnologias Utilizadas

- **Docker** e **Docker Compose**
- **Apache Kafka**
- **Apache Spark Structured Streaming**
- **Delta Lake**
- **Python 3.9**
- **Kafka-Python**

---

## ⚙️ Arquitetura

```plaintext
+------------------+       +----------------------+       +----------------------+
|   iot_producer   | --->  |    Apache Kafka      | --->  | Apache Spark + Delta |
| (simula sensores)|       | (mensageria em tempo)|       | (streaming + persist)|
+------------------+       +----------------------+       +----------------------+
```

---

## 🚀 Como Executar

> Requisitos: Docker e Docker Compose instalados

### 1. Crie a rede Docker (apenas uma vez)

```bash
docker network create iot_kafka_network
```

---

### 2. Suba os containers

#### Em um terminal (Kafka + Zookeeper + Producer):
```bash
docker-compose -f docker-compose.kafka.yml up --build
```

#### Em outro terminal (Spark):
```bash
docker-compose -f docker-compose.spark.yml up --build
```

---

### 3. Consulta dos dados persistidos

Depois que o pipeline estiver rodando, execute:

```PowerShell
docker exec -it spark spark-submit --packages io.delta:delta-core_2.12:2.4.0 /app/query_data.py
```

---

### 4. Para parar os serviços

```bash
# Parar Kafka e Producer
docker-compose -f docker-compose.kafka.yml down -v

# Parar Spark
docker-compose -f docker-compose.spark.yml down -v
```



---

## 📒 Sobre

Este projeto tem como objetivo demonstrar, de forma prática, o fluxo completo de ingestão de dados em tempo real em um cenário comum em **instituições financeiras**, **telemetria industrial** ou **monitoramento ambiental**, aplicando boas práticas de engenharia de dados com foco em:

- Processamento em streaming
- Armazenamento escalável e confiável com Delta Lake
- Integração modular usando containers

---

## ✍️ Autor

Kelvin Soares Gomes  
[github.com/Kelvin-SG98](https://github.com/Kelvin-SG98)  
Engenheiro de Dados | Apaixonado por arquitetura de dados e projetos práticos

---