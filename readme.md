# Discord chatbot with Rasa
## Rock-Paper-Scissors

----
### Installation

1. Create discord bot and generate token
2. Paste token in docker-compose.yml `BOT_TOKEN` environment variable
3. Run command to train model: 
```bash
docker run --rm -v $(pwd):/app khalosa/rasa-aarch64:3.5.2 train
```
4. Run docker compose:
```bash
docker compose up -d
```