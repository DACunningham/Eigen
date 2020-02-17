import os

import app.nlp.FileIO
import app.nlp.TextProcessor
import app.nlp.KeyWordExtractor
import app.nlp.Term
#from FileIO import FileIO
#from TextProcessor import TextProcessor
#from KeyWordExtractor import KeyWordExtractor
#from Term import Term

class InterestingWordManager(object):
    """description of class"""

    def __init__(self, *args, **kwargs):
        self.file_io = FileIO()
        self.text_processor = TextProcessor()
        self.keyword_extractor = KeyWordExtractor()

        self.file_paths = ["resources/doc1.txt", "resources/doc2.txt", "resources/doc3.txt", 
                           "resources/doc4.txt", "resources/doc5.txt", "resources/doc6.txt" ]
        self.document_library = file_io.load_many_text_files(self.filePaths)
        self.processed_text_documents = []
        self.sorted_important_words_by_count = {}
        self.documents_sentences = {}

        return super().__init__(*args, **kwargs)
    
    def process_documents(self, _document_library, _text_processor):
        processed_word_library = []
        processed_doc_library = []
        for document in _document_library:
            processed_word_library.append(_text_processor.preprocessor(document))

        for document in processed_word_library:
            processed_doc_library.append(_text_processor.stringifyTokenArray(document))
        return processed_doc_library
    
    def get_sorted_important_words(self, _document_library, _keyword_extractor, _processed_text_documents):
        temp_doc_results = []
        sorted_important_words = {}
        for index in range(len(_document_library)):
            temp_doc_results.append(_keyword_extractor.get_highest_word_count(index, _processed_text_documents))

        for item in temp_doc_results:
            for key in item:
                sorted_important_words[key] = document_results[key]

        sorted_important_words = sorted(sorted_important_words.items(), key=lambda x:x[1], reverse = True)
        print(sorted_important_words)
        return sorted_important_words

    def get_document_sentences(self, _text_processor, _document_library):
        document_sentences = {}
        for index in range(len(filePaths)):
            file_name = os.path.basename(filePaths[index])
            document_sentences[file_name] = _text_processor.convert_to_sentences(_document_library[index])
        return document_sentences

    def get_interesting_terms_docs_sentences(self, sorted_important_words, documents_sentences):
        terms = []
        for term in sorted_important_words:
            temp_term = Term(term[0], term[1])
            for key in documents_sentences:
                term_count_in_document = 0
                for sentence in documents_sentences[key]:
                    if term[0] in sentence.casefold():
                        temp_term.term_in_sentences.append(sentence)
                        term_count_in_document += 1
                        if term_count_in_document == 1:
                            temp_term.term_in_documents.append(key)
            terms.append(temp_term)

        print("----------------------------------------")
        print(terms[0].term)
        print(terms[0].total_term_count)
        print(terms[0].term_in_documents)
        print(terms[0].term_in_sentences)
        return terms

    def get_interesting_terms(self):
        self.processed_text_documents = process_documents(self.document_library)
        self.sorted_important_words_by_count = get_sorted_important_words(self.document_library, self.keyword_extractor, self.processed_text_documents)
        self.documents_sentences = get_document_sentences(self.text_processor, self.document_library)
        return get_interesting_terms_docs_sentences(self.sorted_important_words_by_count, self.documents_sentences)