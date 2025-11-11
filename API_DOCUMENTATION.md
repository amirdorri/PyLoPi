# PyLoPi API Documentation

Complete REST API reference for PyLoPi v1.0.0

## Base URL

```
http://localhost:5000
```

## Authentication

Currently, PyLoPi does not require authentication. This will be added in future versions.

---

## Endpoints

### 1. Get Configuration

Retrieve current system configuration.

**Endpoint:** `GET /api/config`

**Response:**
```json
{
    "language": "en",
    "email_notifications": false,
    "email_address": "",
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "smtp_username": "",
    "smtp_password": "",
    "enabled_error_types": [
        "SyntaxError",
        "TypeError",
        "ValueError"
    ],
    "log_retention_days": 30,
    "max_logs_per_file": 10000,
    "monitoring_interval": 2
}
```

**Example:**
```bash
curl http://localhost:5000/api/config
```

```python
import requests
response = requests.get('http://localhost:5000/api/config')
config = response.json()
```

---

### 2. Update Configuration

Update system configuration settings.

**Endpoint:** `POST /api/config`

**Request Body:**
```json
{
    "language": "fa",
    "email_notifications": true,
    "email_address": "user@example.com",
    "enabled_error_types": ["SyntaxError", "TypeError"]
}
```

**Response:**
```json
{
    "status": "success"
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/config \
  -H "Content-Type: application/json" \
  -d '{"language": "en", "email_notifications": true}'
```

```python
import requests
config = {
    "email_notifications": True,
    "email_address": "user@example.com"
}
response = requests.post('http://localhost:5000/api/config', json=config)
```

---

### 3. Start Monitoring

Start monitoring specified log files.

**Endpoint:** `POST /api/start-monitoring`

**Request Body:**
```json
{
    "log_paths": [
        "/var/log/app.log",
        "/var/log/error.log"
    ]
}
```

**Response:**
```json
{
    "status": "success"
}
```

**Error Response:**
```json
{
    "status": "error",
    "message": "No log paths provided"
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/start-monitoring \
  -H "Content-Type: application/json" \
  -d '{"log_paths": ["/var/log/app.log"]}'
```

```python
import requests
data = {
    "log_paths": ["/var/log/app.log", "/var/log/error.log"]
}
response = requests.post('http://localhost:5000/api/start-monitoring', json=data)
```

---

### 4. Stop Monitoring

Stop the log monitoring process.

**Endpoint:** `POST /api/stop-monitoring`

**Response:**
```json
{
    "status": "success"
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/stop-monitoring
```

```python
import requests
response = requests.post('http://localhost:5000/api/stop-monitoring')
```

---

### 5. Get Recent Logs

Retrieve recent log entries.

**Endpoint:** `GET /api/logs?limit=50`

**Query Parameters:**
- `limit` (optional): Number of logs to return (default: 50)

**Response:**
```json
[
    {
        "id": 1,
        "timestamp": "2024-11-11 10:30:45",
        "log_file": "/var/log/app.log",
        "error_type": "TypeError",
        "error_message": "unsupported operand type(s)",
        "short_analysis": "Type mismatch error: unsupported operand...",
        "severity": "high",
        "status": "new"
    },
    {
        "id": 2,
        "timestamp": "2024-11-11 10:35:12",
        "log_file": "/var/log/app.log",
        "error_type": "SyntaxError",
        "error_message": "invalid syntax at line 42",
        "short_analysis": "Syntax error detected in the code...",
        "severity": "low",
        "status": "new"
    }
]
```

**Example:**
```bash
curl http://localhost:5000/api/logs?limit=10
```

```python
import requests
response = requests.get('http://localhost:5000/api/logs', params={'limit': 10})
logs = response.json()

for log in logs:
    print(f"{log['error_type']}: {log['error_message']}")
```

---

### 6. Get Log Details

Get complete details for a specific log entry.

**Endpoint:** `GET /api/log/<log_id>`

**Path Parameters:**
- `log_id`: Integer ID of the log entry

**Response:**
```json
{
    "id": 1,
    "timestamp": "2024-11-11 10:30:45",
    "log_file": "/var/log/app.log",
    "error_type": "TypeError",
    "error_message": "unsupported operand type(s) for +: 'int' and 'str'",
    "full_log": "[2024-11-11 10:30:45] TypeError: unsupported operand type(s) for +: 'int' and 'str'",
    "analysis": "Type mismatch error: unsupported operand type(s) for +: 'int' and 'str'. This occurs when an operation is performed on incompatible data types.",
    "solution": "Ensure all variables are of the expected type. Use type conversion functions if needed.\n\nCommon solutions:\n1. Convert string to int: int('123')\n2. Convert int to string: str(123)\n3. Check types before operations",
    "code_fix": "value = str(value)\nresult = int(input(\"Enter number: \"))",
    "severity": "high",
    "status": "new"
}
```

**Error Response:**
```json
{
    "error": "Log not found"
}
```

**Example:**
```bash
curl http://localhost:5000/api/log/1
```

```python
import requests
log_id = 1
response = requests.get(f'http://localhost:5000/api/log/{log_id}')
log_detail = response.json()

print(f"Error: {log_detail['error_type']}")
print(f"Analysis: {log_detail['analysis']}")
print(f"Solution: {log_detail['solution']}")
```

---

### 7. Get Statistics

Retrieve system statistics and analytics.

**Endpoint:** `GET /api/stats`

**Response:**
```json
{
    "total_logs": 142,
    "today_count": 23,
    "top_errors": [
        {
            "error_type": "TypeError",
            "count": 45
        },
        {
            "error_type": "ValueError",
            "count": 32
        },
        {
            "error_type": "SyntaxError",
            "count": 28
        }
    ],
    "by_severity": [
        {
            "severity": "critical",
            "count": 5
        },
        {
            "severity": "high",
            "count": 42
        },
        {
            "severity": "medium",
            "count": 67
        },
        {
            "severity": "low",
            "count": 28
        }
    ]
}
```

**Example:**
```bash
curl http://localhost:5000/api/stats
```

```python
import requests
response = requests.get('http://localhost:5000/api/stats')
stats = response.json()

print(f"Total logs: {stats['total_logs']}")
print(f"Today: {stats['today_count']}")
print(f"Top error: {stats['top_errors'][0]['error_type']}")
```

---

### 8. Set Language

Change the interface language.

**Endpoint:** `POST /api/language`

**Request Body:**
```json
{
    "language": "en"
}
```

**Supported Languages:**
- `en` - English
- `fa` - Persian (Farsi)

**Response:**
```json
{
    "status": "success"
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/language \
  -H "Content-Type: application/json" \
  -d '{"language": "fa"}'
```

```python
import requests
data = {"language": "en"}
response = requests.post('http://localhost:5000/api/language', json=data)
```

---

## Error Codes

| Status Code | Description |
|-------------|-------------|
| 200 | Success |
| 400 | Bad Request - Invalid parameters |
| 404 | Not Found - Resource doesn't exist |
| 500 | Internal Server Error |

---

## Data Models

### Log Entry Model

```json
{
    "id": "integer",
    "timestamp": "string (ISO 8601)",
    "log_file": "string (file path)",
    "error_type": "string",
    "error_message": "string",
    "full_log": "string",
    "analysis": "string",
    "solution": "string",
    "code_fix": "string",
    "severity": "string (critical|high|medium|low)",
    "status": "string (new|reviewed|resolved)"
}
```

### Configuration Model

```json
{
    "language": "string (en|fa)",
    "email_notifications": "boolean",
    "email_address": "string (email)",
    "smtp_server": "string",
    "smtp_port": "integer",
    "smtp_username": "string",
    "smtp_password": "string",
    "enabled_error_types": ["array of strings"],
    "log_retention_days": "integer",
    "max_logs_per_file": "integer",
    "monitoring_interval": "integer (seconds)"
}
```

---

## Example Integration

### Python Integration

```python
import requests
import time

class PyLopiClient:
    def __init__(self, base_url='http://localhost:5000'):
        self.base_url = base_url
    
    def start_monitoring(self, log_paths):
        response = requests.post(
            f'{self.base_url}/api/start-monitoring',
            json={'log_paths': log_paths}
        )
        return response.json()
    
    def get_recent_logs(self, limit=50):
        response = requests.get(
            f'{self.base_url}/api/logs',
            params={'limit': limit}
        )
        return response.json()
    
    def get_log_detail(self, log_id):
        response = requests.get(f'{self.base_url}/api/log/{log_id}')
        return response.json()
    
    def get_stats(self):
        response = requests.get(f'{self.base_url}/api/stats')
        return response.json()

client = PyLopiClient()
client.start_monitoring(['/var/log/app.log'])

while True:
    logs = client.get_recent_logs(limit=10)
    for log in logs:
        print(f"New error: {log['error_type']}")
    time.sleep(30)
```

### JavaScript Integration

```javascript
class PyLopiClient {
    constructor(baseUrl = 'http://localhost:5000') {
        this.baseUrl = baseUrl;
    }
    
    async startMonitoring(logPaths) {
        const response = await fetch(`${this.baseUrl}/api/start-monitoring`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ log_paths: logPaths })
        });
        return response.json();
    }
    
    async getRecentLogs(limit = 50) {
        const response = await fetch(`${this.baseUrl}/api/logs?limit=${limit}`);
        return response.json();
    }
    
    async getLogDetail(logId) {
        const response = await fetch(`${this.baseUrl}/api/log/${logId}`);
        return response.json();
    }
    
    async getStats() {
        const response = await fetch(`${this.baseUrl}/api/stats`);
        return response.json();
    }
}

const client = new PyLopiClient();
await client.startMonitoring(['/var/log/app.log']);

const logs = await client.getRecentLogs(10);
console.log('Recent errors:', logs);
```

---

## Rate Limiting

Currently, there are no rate limits. This may change in future versions.

## Webhooks

Webhook support is planned for future releases.

## Support

For API support and questions:
- Email: picobaz3@gmail.com