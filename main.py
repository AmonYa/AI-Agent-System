from core.model_loader import load_model
from core.logger import logger

# Загружаем модель
model, tokenizer = load_model()
logger.info("Модель загружена успешно!")

def chat():
    """Чат с WhiteRabbitNeo"""
    print("\n💬 WhiteRabbitNeo запущен. Введите 'выход' для завершения.")
    while True:
        user_input = input("🧑‍💻 Ты: ")
        if user_input.lower() in ["выход", "exit"]:
            print("👋 Чат завершен.")
            break

        inputs = tokenizer(user_input, return_tensors="pt").to("cuda")
        output = model.generate(**inputs, max_new_tokens=100)
        response = tokenizer.decode(output[0], skip_special_tokens=True)

        print(f"🤖 WhiteRabbitNeo: {response}")
        logger.info(f"Ты: {user_input} | Ответ: {response}")

if __name__ == "__main__":
    chat()
