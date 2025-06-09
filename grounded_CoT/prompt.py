PRE_TEMPLATE_0 = (
    "You will be provided with two versions of the same infographic chart, each with certain elements highlighted.\n"
)
PRE_TEMPLATE_0_TEXT = (
    "You will also be provided the information lists of elements highlighted in the images. Each entry in the lists of elements follows the format (ID, Content), where:\n"
    "    ID means the id of element.\n"
    "    Content means the content of the element.\n\n"
)
# <First Layer of Image with Boxes>
PRE_TEMPLATE_1 = (
    "This above image highlights non-text elements enclosed in boxes, each labeled with a unique ID.\n"
)
PRE_TEMPLATE_1_TEXT = (
    "Here is the list of elements:\n"
    "***************************************\n"
    "<non-text-element-list>"
    "***************************************\n\n"
)
# <Second Layer of Image with Boxes>
PRE_TEMPLATE_2 = (
    "This above image highlights text elements enclosed in boxes, each labeled with a unique ID.\n"
)
PRE_TEMPLATE_2_TEXT = (
    "Here is the list of elements:\n"
    "***************************************\n"
    "<text-element-list>"
    "***************************************\n\n"
)
PRE_TEMPLATE_3 = (
    "These labeled elements are intended to support you in your upcoming task. Please refer to and make use of them as needed during your thinking and analysis, and be sure to mention their IDs when doing so.\n"
    "For example:\n"
    "1. Based on the content in box ID 1, (your finding about the box), or;\n2. Based on the relationships of box ID 1, ID 2, ..., ID N, (your finding based on the boxes).\n\n"
    "Below is the image of original infographic chart, followed by your formal task:\n"
)
# <Original Image>
PROMPT_TEMPLATES = {
    "Factoid": (
        "You are given a factoid question that you need to answer based on the provided image.\n"
        "You need to think step-by-step, but your final answer should be a single word, number, or phrase. If the question is unanswerable based on the information in the provided image, your answer should be unanswerable. Do not generate units. "
        "But if numerical units such as million, m, billion, B, or K are required, use the exact notation shown in the chart.\n"
        "If there are multiple final answers, put them in brackets using this format ['Answer1', 'Answer2'].\n"
        "Remember to think step-by-step and mention the IDs of the elements you used, and reply in the following JSON format:\n{\n    \"Steps\": \"The step-by-step thinking process with IDs mentioned.\",\n    \"A\": \"Your answer.\"\n}\n"
        "Question: <question>"
    ),
    "Multi Choice": (
        "You are given a question along with different possible answers. You need to select the correct answer from them based on the provided image.\n"
        "You need to think step-by-step, but your final answer should be one of the options letters only: a, b, c or d (just the letter itself without any additional text). If the question is unanswerable based on the information in the provided image, your answer should be unanswerable.\n"
        "If there are multiple final answers, put them in brackets using this format ['Answer1', 'Answer2'].\n"
        "Remember to think step-by-step and mention the IDs of the elements you used, and reply in the following JSON format:\n{\n    \"Steps\": \"The step-by-step thinking process with IDs mentioned.\",\n    \"A\": \"Your answer.\"\n}\n"
        "Question: <question>"
    ),
    "Hypothetical": (
        "You are given a hypothetical question that you need to answer based on the provided image.\n"
        "You need to think step-by-step, but your final answer should be a single word, number, or phrase. If the question is unanswerable based on the information in the provided image, your answer should be unanswerable. Do not generate units. "
        "But if numerical units such as million, m, billion, B, or K are required, use the exact notation shown in the chart.\n"
        "If there are multiple final answers, put them in brackets using this format ['Answer1', 'Answer2'].\n"
        "Remember to think step-by-step and mention the IDs of the elements you used, and reply in the following JSON format:\n{\n    \"Steps\": \"The step-by-step thinking process with IDs mentioned.\",\n    \"A\": \"Your answer.\"\n}\n"
        "Question: <question>"
    ),
    "Fact Checking": (
        "You are given a fact statement that you need to assess based on the provided image.\n"
        "You need to think step-by-step, but your final answer should be either true or false (without any additional text). If the question is unanswerable based on the information in the provided image, your answer should be unanswerable.\n"
        "If there are multiple final answers, put them in brackets using this format ['Answer1', 'Answer2'].\n"
        "Remember to think step-by-step and mention the IDs of the elements you used, and reply in the following JSON format:\n{\n    \"Steps\": \"The step-by-step thinking process with IDs mentioned.\",\n    \"A\": \"Your answer.\"\n}\n"
        "Question: <question>"
    ),
    "Conversational": (
        "You are given a multi - turn conversation, and your job is to answer the final question based on the conversation history and the information in the provided image.\n"
        "You need to think step-by-step, but your final answer should be a single word, number, or phrase. If the question is unanswerable based on the information in the provided image, your answer should be unanswerable. Do not generate units. "
        "But if numerical units such as million, m, billion, B, or K are required, use the exact notation shown in the chart.\n"
        "If there are multiple final answers, put them in brackets using this format ['Answer1', 'Answer2'].\n"
        "Remember to think step-by-step and mention the IDs of the elements you used, and reply in the following JSON format:\n{\n    \"Steps\": \"The step-by-step thinking process with IDs mentioned.\",\n    \"A\": \"Your answer.\"\n}\n"
        "Conversation: <conversation>\nQuestion: <question>"
    ),
}