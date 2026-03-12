from openai import OpenAI

def main():
    client = OpenAI(
        api_key="11e15d4e-e28f-405a-bf27-ce3b51321270",
        base_url="https://ark.cn-beijing.volces.com/api/v3"
    )

    print("✨ DeepSeek 机器人已启动，输入 quit 退出")
    while True:
        user_input = input("你：")
        if user_input.lower() == "quit":
            print("👋 再见")
            break
        response = client.chat.completions.create(
            model="ep-20260312134409-sj7pv",
            messages=[{"role": "user", "content": user_input}]
        )
        print("DeepSeek：", response.choices[0].message.content)

if __name__ == "__main__":
    main()
