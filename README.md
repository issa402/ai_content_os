# AI Content Automation OS

This project is an AI Content Automation OS that automates content creation workflows, from script generation to video assembly and social media posting.

## Project Structure

```
ai_content_os/
├── api-gateway/                # Go service for API gateway
│   ├── handlers/
│   └── main.go
├── orchestration-service/      # Go service for workflow orchestration
│   ├── workflows/
│   └── main.go
├── ingestion-service/          # Go service for content ingestion
│   ├── ingesters/
│   └── main.go
├── ai-services/                # Python services for AI/ML tasks
│   ├── script-intelligence/    # Python service for script generation
│   │   ├── main.py
│   │   └── prompts.py
│   ├── visual-generation/      # Python service for image/video generation
│   │   ├── main.py
│   │   ├── qwen_utils.py
│   │   └── cropping.py
│   └── audio-engine/           # Python service for audio processing
│       └── main.py
├── video-assembly-service/     # Go/Python service for video assembly
│   ├── assemblers/
│   └── main.go
├── posting-service/            # Go service for social media posting
│   ├── posters/
│   └── main.go
├── analytics-service/          # Go service for analytics
│   ├── collectors/
│   └── main.go
├── frontend/                   # Frontend application (placeholder)
│   └── src/
│       └── components/
├── shared/                     # Shared libraries and utilities
│   ├── go/utils/
│   └── python/utils/
├── config/                     # Configuration files
├── scripts/                    # Helper scripts
├── docs/                       # Project documentation
├── Dockerfile                  # Dockerfile for containerization
└── README.md                   # This file
```

## Services

*   **api-gateway (Go):** The single entry point for all client requests.
*   **orchestration-service (Go):** Manages the entire content creation workflow.
*   **ingestion-service (Go):** Ingests content from various sources.
*   **ai-services (Python):** A collection of services for AI-related tasks.
    *   **script-intelligence:** Generates and analyzes scripts.
    *   **visual-generation:** Generates images and videos using Qwen and other models.
    *   **audio-engine:** Handles text-to-speech, voice cloning, and audio processing.
*   **video-assembly-service (Go/Python):** Assembles the final video from various assets.
*   **posting-service (Go):** Posts the generated content to social media platforms.
*   **analytics-service (Go):** Collects and analyzes content performance data.
