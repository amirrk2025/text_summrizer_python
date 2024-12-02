# import openai
#
# # وارد کردن کلید API و URL
# API_KEY = "tpsg-aHF3SU6Ey6wLchUOcnb8SKkSsuEPVso"
# openai.api_key = API_KEY
# openai.api_base = "https://api.metisai.ir/openai/v1"  # اگر از OpenAI رسمی استفاده می‌کنی، این خط رو حذف کن
#
# def summarize_text(long_text):
#     """
#     این تابع یک متن بلند رو می‌گیره و با استفاده از OpenAI خلاصه می‌کنه.
#     """
#     messages_list = [
#         {"role": "system", "content": "You are a helpful assistant that summarizes text."},
#         {"role": "user", "content": f"Please summarize the following text:\n\n{long_text}"}
#     ]
#
#     try:
#
#         print("\n \n \n Connecting to the LLM...")
#         response = openai.ChatCompletion.create(
#             model="gpt-4",  # مدل مورد استفاده (در صورت لزوم تغییر کن)
#             messages=messages_list,
#             temperature=0.5,  # تنظیم خلاقیت پاسخ
#             max_tokens=500    # حداکثر تعداد کلمات خلاصه
#         )
#
#         # استخراج خلاصه از پاسخ
#         summary = response['choices'][0]['message']['content']
#         return summary
#
#     except Exception as e:
#         print(f"Error occurred: {e}")
#         return None
#
#
# if __name__ == "__main__":
#     print("Welcome to the Text Summarizer!")
#     long_text = input("Please paste the long text you want to summarize:\n")
#     summary = summarize_text(long_text)
#     if summary:
#         print("\nSummary:\n")
#         print(summary)







import openai

# وارد کردن کلید API و URL
API_KEY = "tpsg-aHF3SU6Ey6wLchUOcnb8SKkSsuEPVso"
openai.api_key = API_KEY
openai.api_base = "https://api.metisai.ir/openai/v1"  # اگر از OpenAI رسمی استفاده می‌کنی، این خط رو حذف کن

def summarize_text(long_text):
    """
    این تابع یک متن بلند رو می‌گیره و با استفاده از OpenAI خلاصه‌ای متناسب با زبان متن ارائه می‌ده.
    """
    # تشخیص زبان متن
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
            model="gpt-4",  # مدل مورد استفاده (در صورت لزوم تغییر کن)
            messages=messages_list,
            temperature=0.7,  # تنظیم خلاقیت پاسخ (برای توضیح بیشتر مقدار را کمی افزایش دادم)
            max_tokens=700    # افزایش تعداد کلمات برای توضیحات بیشتر
        )

        # استخراج خلاصه از پاسخ
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





















