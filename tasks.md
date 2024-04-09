[View extended tasks](./tasks_extended.md)

## Artificial Languages

|   task_number | instruction                                                                                                                                   | target         |
|--------------:|:----------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
|             1 | Please apply a Caesar cipher with a shift of 5 to the following text: "{InputText}"                                                           | {ModifiedText} |
|             2 | Please convert the following text from its mirror language back to English: "{ModifiedText}"                                                  | {InputText}    |
|             3 | Please convert this Pig Latin text back to English: "{ModifiedText}"                                                                          | {InputText}    |
|             4 | Please convert this text from leetspeak to standard English: "{ModifiedText}"                                                                 | {InputText}    |
|             5 | Insert 'ithag' after each vowel in the following text: "{InputText}"                                                                          | {ModifiedText} |
|             6 | Please convert the following text to its mirror language, where each letter is replaced with its opposite (a<->z, b<->y, etc.): "{InputText}" | {ModifiedText} |
|             7 | Please convert this text to leetspeak: "{InputText}"                                                                                          | {ModifiedText} |
|             8 | Please convert this text to pig latin: "{InputText}"                                                                                          | {ModifiedText} |
|             9 | Please translate the following text into Igpay Atinlay (Pig Latin with 'ay' after each word): "{InputText}"                                   | {ModifiedText} |
|            10 | Please reverse the Caesar cipher with a shift of 5 for the following text: "{ModifiedText}"                                                   | {InputText}    |
|            11 | Shift all vowels forward one in the order aeiou (circularly, so 'u' becomes 'a'): "{InputText}"                                               | {ModifiedText} |

## Character Manipulation

|   task_number | instruction                                                                                                               | target         |
|--------------:|:--------------------------------------------------------------------------------------------------------------------------|:---------------|
|             1 | Please remove all but the first and last character of each word in this text: "{InputText}"                               | {ModifiedText} |
|             2 | Please remove the last letter from each word in this text: "{InputText}"                                                  | {ModifiedText} |
|             3 | Please remove all punctuation from the following text: "{InputText}"                                                      | {ModifiedText} |
|             4 | Please remove all spaces in this text: "{InputText}"                                                                      | {ModifiedText} |
|             5 | Please replace all instances of the character '{Char1}' in the following text with '{Char2}': "{InputText}"               | {ModifiedText} |
|             6 | Please replace all consonants in the following text with asterisks (*): "{InputText}"                                     | {ModifiedText} |
|             7 | Please replace all spaces in the following text with underscores: "{InputText}"                                           | {ModifiedText} |
|             8 | Please replace all vowels in the following text with asterisks (*): "{InputText}"                                         | {ModifiedText} |
|             9 | Please reverse the character order in every third word of the following text, starting with the first word: "{InputText}" | {ModifiedText} |
|            10 | Please reverse character order in every other word in this text, starting with the first word: "{InputText}"              | {ModifiedText} |
|            11 | Please swap the case of all letters in the following text: "{InputText}"                                                  | {ModifiedText} |

## Composite Transformations

|   task_number | instruction                                                                                                                                   | target         |
|--------------:|:----------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
|             1 | Please change each letter to alternate case starting with lowercase, shuffle the words, and then reverse the string: "{InputText}"            | {ModifiedText} |
|             2 | Please double each letter in the text and then reverse the entire string: "{InputText}"                                                       | {ModifiedText} |
|             3 | Please encode each word in the text as its ASCII value, separated by dashes, then reverse the order of these codes: "{InputText}"             | {ModifiedText} |
|             4 | Extract the initials of each word, concatenate them, and reverse the string: "{InputText}"                                                    | {ModifiedText} |
|             5 | For each word in the text, interleave it with its reverse and then reverse the entire sentence order: "{InputText}"                           | {ModifiedText} |
|             6 | Please remove all but the first and last word of each sentence, then reverse the order of the remaining sentences in this text: "{InputText}" | {ModifiedText} |
|             7 | Please remove all but the first letter of each word, then reverse the order of the words in this text: "{InputText}"                          | {ModifiedText} |
|             8 | Please remove all but the last letter of each word, then reverse the resulting string: "{InputText}"                                          | {ModifiedText} |
|             9 | Remove all vowels from the text, duplicate the remaining consonants, and then reverse the string: "{InputText}"                               | {ModifiedText} |
|            10 | Please replace each word in this text with its length, then reverse the resulting string: "{InputText}"                                       | {ModifiedText} |
|            11 | Please reverse the order of words and remove all spaces in this text: "{InputText}"                                                           | {ModifiedText} |
|            12 | Please scramble the inner letters of each word, leaving the first and last letters intact, then reverse the order of the words: "{InputText}" | {ModifiedText} |

## Language Understanding

|   task_number | instruction                                                                                                                                                                                                | target      |
|--------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
|             1 | Please add commas back into the following text at appropriate places: "{ModifiedText}"                                                                                                                     | {InputText} |
|             2 | Vowels have been removed from the following text: "{ModifiedText}". Please add back the dropped vowels to restore the complete sentence.                                                                   | {InputText} |
|             3 | Please add spaces back into the following text where they are missing: "{ModifiedText}"                                                                                                                    | {InputText} |
|             4 | The words in the following text have been merged into a single block without spaces: "{ModifiedText}". Please separate them back into the original sentence.                                               | {InputText} |
|             5 | Letters in some words of the following text have been unnecessarily duplicated: "{ModifiedText}". Please remove the duplicates to restore the original text.                                               | {InputText} |
|             6 | One character in this text has been changed to another character. Identify the change and reconstruct the original sentence: "{ModifiedText}"                                                              | {InputText} |
|             7 | Please reorder the words in the following text to form coherent sentences: "{ModifiedText}"                                                                                                                | {InputText} |
|             8 | All instances of the letter '{Char1}' have been removed from the following text: "{ModifiedText}". Please restore the complete sentence by inserting the letter '{Char1}' back into the correct positions. | {InputText} |
|             9 | Punctuation has been removed from the following text: "{ModifiedText}". Please add the punctuation back into the text where it belongs.                                                                    | {InputText} |
|            10 | A word in the following sentence is scrambled: "{ModifiedText}". Please identify the scrambled word, unscramble it, and provide the correct sentence.                                                      | {InputText} |
|            11 | Please reorder the following scrambled words to form coherent sentences: "{ModifiedText}"                                                                                                                  | {InputText} |

## Letter Analysis

|   task_number | instruction                                                                                                                                                              | target         |
|--------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
|             1 | Please add a number in parentheses after each word in this text indicating its position: "{InputText}"                                                                   | {ModifiedText} |
|             2 | Please count the number of consonants in the following text: "{InputText}"                                                                                               | {ModifiedText} |
|             3 | Please count the number of lowercase letters in the following text: "{InputText}"                                                                                        | {ModifiedText} |
|             4 | Count the number of unique letters in the following text. Exclude numbers and special characters: "{InputText}"                                                          | {ModifiedText} |
|             5 | Please count the number of uppercase letters in the following text: "{InputText}"                                                                                        | {ModifiedText} |
|             6 | Please count the number of vowels in the following text: "{InputText}"                                                                                                   | {ModifiedText} |
|             7 | Identify all unique letters used in the following text: "{InputText}"                                                                                                    | {ModifiedText} |
|             8 | Identify the first letter in the following text that does not repeat. If all letters repeat, return an empty response: "{InputText}"                                     | {ModifiedText} |
|             9 | Find the last letter that appears more than once in the following text. If no letter repeats, return an empty response: "{InputText}"                                    | {ModifiedText} |
|            10 | Find the first letter that appears exactly 3 times in the following text. Provide the letter. If no letter meets this condition, return an empty response: "{InputText}" | {ModifiedText} |
|            11 | Find how many letters appear exactly N times in the following text. Provide the count: "{InputText}"                                                                     | {ModifiedText} |

## Sentence Manipulation

|   task_number | instruction                                                                                                                                         | target         |
|--------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
|             1 | Please add the word 'Note:' to the beginning of each sentence in the following text: "{InputText}"                                                  | {ModifiedText} |
|             2 | Please alternate the case of letters in each sentence starting with uppercase for the first sentence and so on in the following text: "{InputText}" | {ModifiedText} |
|             3 | Please concatenate all sentences in reverse order into one continuous text in the following text: "{InputText}"                                     | {ModifiedText} |
|             4 | Please number each sentence sequentially starting with 1 in the following text: "{InputText}"                                                       | {ModifiedText} |
|             5 | Please remove the first and last word from each sentence in this text: "{InputText}"                                                                | {ModifiedText} |
|             6 | Please remove the second and second-to-last word from each sentence in this text: "{InputText}"                                                     | {ModifiedText} |
|             7 | Please remove all sentences with 3 words or fewer and 10 words or more from the following text: "{InputText}"                                       | {ModifiedText} |
|             8 | Please reverse the order of characters in each sentence of the following text, while keeping the original sentence order: "{InputText}"             | {ModifiedText} |
|             9 | Please reverse the order of sentences in the following text: "{InputText}"                                                                          | {ModifiedText} |
|            10 | Please reverse the word order in each sentence of the following text, while keeping the original sentence order: "{InputText}"                      | {ModifiedText} |
|            11 | Please sort all the sentences in the following text by their length, from shortest to longest: "{InputText}"                                        | {ModifiedText} |

## Text Analysis

|   task_number | instruction                                                                                                  | target         |
|--------------:|:-------------------------------------------------------------------------------------------------------------|:---------------|
|             1 | Please count the number of words in this text: "{InputText}"                                                 | {ModifiedText} |
|             2 | Please remove all words with 7 letters or more from the following text: "{InputText}"                        | {ModifiedText} |
|             3 | Please remove all words with 3 letters or fewer and 7 letters or more from the following text: "{InputText}" | {ModifiedText} |
|             4 | Please remove all words with 3 letters or fewer from the following text: "{InputText}"                       | {ModifiedText} |
|             5 | Please remove all words with odd length from this text: "{InputText}"                                        | {ModifiedText} |
|             6 | Please replace each word with its index in the sentence in this text: "{InputText}"                          | {ModifiedText} |
|             7 | Please replace each word with its last two letters in this text: "{InputText}"                               | {ModifiedText} |
|             8 | Please replace each word with its length in this text: "{InputText}"                                         | {ModifiedText} |
|             9 | Please sort all the words in the following text alphabetically: "{InputText}"                                | {ModifiedText} |
|            10 | Please sort all the words in the following text by their length, from shortest to longest: "{InputText}"     | {ModifiedText} |
|            11 | Please sort all the words in the following text by their number of vowels, from least to most: "{InputText}" | {ModifiedText} |

## Text Extraction

|   task_number | instruction                                                                                                   | target         |
|--------------:|:--------------------------------------------------------------------------------------------------------------|:---------------|
|             1 | Please extract all consonants from the following text: "{InputText}"                                          | {ModifiedText} |
|             2 | Please extract the first word from each sentence in the following text: "{InputText}"                         | {ModifiedText} |
|             3 | Please extract all unique words from the following text, disregarding case: "{InputText}"                     | {ModifiedText} |
|             4 | Please extract all vowels from the following text: "{InputText}"                                              | {ModifiedText} |
|             5 | Please identify all words in this text that contain the letter '{Char1}': "{InputText}"                       | {ModifiedText} |
|             6 | Please find all words in this text that end with the letter '{Char1}': "{InputText}"                          | {ModifiedText} |
|             7 | Please extract all words in this text that are longer than 5 letters: "{InputText}"                           | {ModifiedText} |
|             8 | Please extract all words from the following text where the first and last letters are the same: "{InputText}" | {ModifiedText} |
|             9 | Please extract all words from the following text that start with a vowel: "{InputText}"                       | {ModifiedText} |
|            10 | Please extract all words from the following text that have an even number of characters: "{InputText}"        | {ModifiedText} |
|            11 | Please extract all words in this text that do not contain the letter '{Char1}': "{InputText}"                 | {ModifiedText} |

## Text Formatting

|   task_number | instruction                                                                                                                           | target         |
|--------------:|:--------------------------------------------------------------------------------------------------------------------------------------|:---------------|
|             1 | Please create an acronym from the following text by taking the first letter of each word and capitalizing it: "{InputText}"           | {ModifiedText} |
|             2 | Please make every fourth word bold in this text by using Markdown syntax: "{InputText}"                                               | {ModifiedText} |
|             3 | Please capitalize all words in this text: "{InputText}"                                                                               | {ModifiedText} |
|             4 | Please capitalize every fourth word in this text, starting with the first word: "{InputText}"                                         | {ModifiedText} |
|             5 | Please capitalize every other word in this text, starting with the first word: "{InputText}"                                          | {ModifiedText} |
|             6 | Please convert this text to camel case: "{InputText}"                                                                                 | {ModifiedText} |
|             7 | Please convert every third word to inline code in Markdown in this text: "{InputText}"                                                | {ModifiedText} |
|             8 | Please create a Markdown bullet list, where each item is a sentence from the following text: "{InputText}"                            | {ModifiedText} |
|             9 | Please italicize and bold alternate words in this text using Markdown syntax, starting with italicizing the first word: "{InputText}" | {ModifiedText} |
|            10 | Please italicize every third word in this text by using Markdown syntax: "{InputText}"                                                | {ModifiedText} |
|            11 | Please strike through every fifth word in this text by using Markdown syntax: "{InputText}"                                           | {ModifiedText} |

## Word Manipulation

|   task_number | instruction                                                                                          | target         |
|--------------:|:-----------------------------------------------------------------------------------------------------|:---------------|
|             1 | Please alternate the casing of words in this text, starting with lowercase: "{InputText}"            | {ModifiedText} |
|             2 | Please capitalize every third word in this text, starting with the first word: "{InputText}"         | {ModifiedText} |
|             3 | Please double each word in the following text: "{InputText}"                                         | {ModifiedText} |
|             4 | Please double every vowel in the following text: "{InputText}"                                       | {ModifiedText} |
|             5 | Please remove all but the first and last word from this text: "{InputText}"                          | {ModifiedText} |
|             6 | Please remove every other word from the following text, starting with the second word: "{InputText}" | {ModifiedText} |
|             7 | Please remove all words containing '{Char1}' from this text: "{InputText}"                           | {ModifiedText} |
|             8 | Please remove all words that are shorter than 4 letters in this text: "{InputText}"                  | {ModifiedText} |
|             9 | Please replace all vowels in the following text with asterisks: "{InputText}"                        | {ModifiedText} |
|            10 | Please reverse the letters of each word in the following text: "{InputText}"                         | {ModifiedText} |
|            11 | Please reverse the order of letters in every second word in this text: "{InputText}"                 | {ModifiedText} |

