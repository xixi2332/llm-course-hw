from openai import OpenAI

# 初始化客户端
client = OpenAI(
    api_key="11e15d4e-e28f-405a-bf27-ce3b51321270",  # 替换成你的 API Key
    base_url="https://ark.cn-beijing.volces.com/api/v3"
)

def chat_with_deepseek(question):
    # 发送请求
    response = client.chat.completions.create(
        model="ep-20260312134409-sj7pv",  # 替换成你的模型接入点 ID
        messages=[{"role": "user", "content": question}]
    )
    # 返回模型回答
    return response.choices[0].message.content

if __name__ == "__main__":
    # 测试对话
    user_input = input("请输入你的问题：")
    answer = chat_with_deepseek(user_input)
    print("DeepSeek 回答：", answer)
