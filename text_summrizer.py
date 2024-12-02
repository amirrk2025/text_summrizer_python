# این برنامه یک متن بلند رو از کاربر میگیره و با خوندن اون خلاصه ای از اون متن بلند به کاربر ارائه میده.


import openai

API_KEY = "your_api_key"
openai.api_key = API_KEY
openai.api_base = "URL"  
def summarize_text(long_text):
 
    is_persian = any("\u0600" <= char <= "\u06FF" for char in long_text)
    if is_persian:
        system_prompt = "شما یک دستیار مفید هستید که متن‌های فارسی را خلاصه می‌کنید و توضیحات کافی ارائه می‌دهید."
        user_prompt = f"لطفاً متن زیر را خلاصه کنید و توضیحات کافی ارائه دهید:\n\n{long_text}"
    else:
        system_prompt = "You are a helpful assistant that summarizes texts in English with sufficient details."
        user_prompt = f"Please summarize the following text with sufficient details:\n\n{long_text}"

    messages_list = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    try:
        print("\n \n \n Connecting to the LLM...")
        response = openai.ChatCompletion.create(
            model="gpt-4", 
            messages=messages_list,
            temperature=0.7, 
            max_tokens=700  
        )

        summary = response['choices'][0]['message']['content']
        return summary

    except Exception as e:
        print(f"Error occurred: {e}")
        return None


if __name__ == "__main__":
    print("Welcome to the Text Summarizer!")
    long_text = input("Please paste the long text you want to summarize:\n")
    summary = summarize_text(long_text)
    if summary:
        print("\nSummary:\n")
        print(summary)





















