import textstat
import string

llm_output_default = '''
The intricate systems that govern our planet are a testament to the complex interplay of biology, chemistry, and physics. Consider the Amazon rainforest, often called the "lungs of the Earth." This vast ecosystem is a crucible of biodiversity, home to millions of species of insects, plants, fish, and mammals, many yet to be discovered. The process of photosynthesis occurs on an unimaginable scale, absorbing immense quantities of carbon dioxide from the atmosphere and releasing the oxygen we depend on. This delicate biological balance is under constant threat from deforestation, which in turn exacerbes global climate change. Understanding this ecosystem requires not just biology, but also advanced remote sensing technology.
'''

llm_more_accessible_output = '''
Our world is full of amazing connections, like a giant puzzle. Think about the Amazon rainforest! People call it the "lungs of the Earth." It's a huge jungle filled with millions of different bugs, plants, fish, and animals. Lots of them haven't even been discovered yet! The plants and trees do something cool called photosynthesis. They breathe in a gas called carbon dioxide (which we breathe out) and breathe out the oxygen we need to live. But this wonderful place is in danger because people are cutting down the trees. This is bad for the forest and also makes the whole planet get warmer. To watch over the forest, scientists use special cameras from space.
'''

llm_less_accessible_output = '''
The convoluted biogeochemical frameworks that modulate our planet serve as a testament to the multifaceted synergistic interactions of biology, chemistry, and physics. Consider the Amazonian rainforest, colloquially designated the "primary terrestrial biogeochemical engine." This expansive biome functions as a nexus of macro-evolutionary diversification, hosting innumerable taxa of insects, flora, fish, and mammals, a significant portion remaining uncatalogued. The process of photosynthetic carbon fixation proceeds at a prodigious magnitude, sequestering substantial volumes of atmospheric carbon dioxide whilst liberating the diatomic oxygen upon which complex life depends. This precarious homeostatic equilibrium exists under perpetual jeopardy from anthropogenic silvicultural clearing, which in turn amplifies global climatological perturbations. Comprehending this biome necessitates not merely biological sciences, but also sophisticated geospatial surveillance methodologies.
'''

def get_cleaned_words(text):
    """Helper function to get a list of words, lowercase and without punctuation."""
    text = text.replace('-', ' ')
    cleaned_text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = cleaned_text.split()
    return words

def count_words(text):
    """Counts the total number of words in the text."""
    words = get_cleaned_words(text)
    return len(words)

def count_sentences(text):
    """Counts the number of sentences using textstat for robustness."""
    return textstat.sentence_count(text)

def count_characters(text):
    """Counts the total number of characters, including spaces and punctuation."""
    return len(text)

def count_unique_words(text):
    """Counts the number of unique (distinct) words in the text."""
    words = get_cleaned_words(text)
    unique_words = set(words)
    return len(unique_words)

def average_word_length(text):
    """Calculates the average length of words in the text."""
    words = get_cleaned_words(text)
    total_length = sum(len(word) for word in words)
    return total_length / len(words) if words else 0

def calculate_readability_metrics(text):
    """Calculates Flesch-Kincaid Grade Level and Flesch Reading Ease."""
    grade_level = textstat.flesch_kincaid_grade(text)
    reading_ease = textstat.flesch_reading_ease(text)
    return grade_level, reading_ease

# --- Analysis Section ---
grade_level_default, reading_ease_default = calculate_readability_metrics(llm_output_default)
grade_level_more_accessible, reading_ease_more_accessible = calculate_readability_metrics(llm_more_accessible_output)
grade_level_less_accessible, reading_ease_less_accessible = calculate_readability_metrics(llm_less_accessible_output)

print("LLM Output Default:")
print("Word Count:", count_words(llm_output_default))
print("Sentence Count:", count_sentences(llm_output_default))
print("Character Count:", count_characters(llm_output_default))
print("Unique Word Count:", count_unique_words(llm_output_default))
print("Average Word Length:", average_word_length(llm_output_default))
print("Flesch-Kincaid Grade Level:", grade_level_default)
print("Flesch Reading Ease:", reading_ease_default)

print("\nLLM More Accessible Output Analysis:")
print("Word Count:", count_words(llm_more_accessible_output))
print("Sentence Count:", count_sentences(llm_more_accessible_output))
print("Character Count:", count_characters(llm_more_accessible_output))
print("Unique Word Count:", count_unique_words(llm_more_accessible_output))
print("Average Word Length:", average_word_length(llm_more_accessible_output))
print("Flesch-Kincaid Grade Level:", grade_level_more_accessible)
print("Flesch Reading Ease:", reading_ease_more_accessible)

print("\nLLM Less Accessible Output Analysis:")
print("Word Count:", count_words(llm_less_accessible_output))
print("Sentence Count:", count_sentences(llm_less_accessible_output))
print("Character Count:", count_characters(llm_less_accessible_output))
print("Unique Word Count:", count_unique_words(llm_less_accessible_output))
print("Average Word Length:", average_word_length(llm_less_accessible_output))
print("Flesch-Kincaid Grade Level:", grade_level_less_accessible)
print("Flesch Reading Ease:", reading_ease_less_accessible)
