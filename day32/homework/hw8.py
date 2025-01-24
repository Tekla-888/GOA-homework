def split_paragraph_into_sentences(paragraph):
  sentences = paragraph.split('.')
  return sentences
paragraph = "This is an example paragraph. It consists of several sentences. Each sentence ends with a period."
sentences_list = split_paragraph_into_sentences(paragraph)
print(sentences_list)