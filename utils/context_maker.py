

async def lessons_context(lesson):
    context = ""
    content = "\n".join([f"▫️{i}" for i in lesson['content']])
    context += f"<b>{lesson['title']}</b>\n\n"
    context += content

    return context