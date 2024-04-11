[View extended tasks](./tasks_extended.md)

## Artificial Languages

|   # | instruction                                                                                                                                                                                                  | claude_2_1_cedar   | beaver   | llama_2_70b_chat   | capybara   |
|----:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|:---------|:-------------------|:-----------|
|   1 | Apply a Caesar cipher with a shift of 5 to the following text. Preserve case, and leave non-alphabetic characters unchanged: "{InputText}"                                                                   | 🟢                 | 🔴       | 🔴                 | 🔴         |
|   2 | Convert the following text from its mirror language back to English: "{ModifiedText}"                                                                                                                        | 🟢                 | 🔴       | 🔴                 | 🔴         |
|   3 | Convert the text from mirror language, where each lowercase letter a-z is mirrored across 'm' and 'n'. Uppercase and non-alphabetic characters remain unchanged. Restore the text to English: {ModifiedText} | 🟢                 | 🔴       | 🔴                 | 🔴         |
|   4 | Convert this Pig Latin text back to English: "{ModifiedText}"                                                                                                                                                | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   5 | Convert this text from leetspeak to standard English: "{ModifiedText}"                                                                                                                                       | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   6 | Insert 'ithag' after each vowel in the following text: "{InputText}"                                                                                                                                         | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   7 | Convert the following text to its mirror language, where each letter is replaced with its opposite (a<->z, b<->y, etc.): "{InputText}"                                                                       | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   8 | Convert this text to leetspeak: "{InputText}"                                                                                                                                                                | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   9 | Convert this text to pig latin: "{InputText}"                                                                                                                                                                | 🔴                 | 🔴       | 🔴                 | 🔴         |
|  10 | Translate the following text into Igpay Atinlay (Pig Latin with 'ay' after each word): "{InputText}"                                                                                                         | 🔴                 | 🔴       | 🔴                 | 🔴         |
|  11 | Reverse the Caesar cipher with a shift of 5 for the following text: "{ModifiedText}"                                                                                                                         | 🔴                 | 🔴       | 🔴                 | 🔴         |
|  12 | Shift all vowels forward one in the order aeiou (circularly, so 'u' becomes 'a'): "{InputText}"                                                                                                              | 🔴                 | 🔴       | 🔴                 | 🔴         |

## Character Manipulation

|   # | instruction                                                                                                        | claude_2_1_cedar   | beaver   | llama_2_70b_chat   | capybara   |
|----:|:-------------------------------------------------------------------------------------------------------------------|:-------------------|:---------|:-------------------|:-----------|
|   1 | Remove all but the first and last character of each word in this text: "{InputText}"                               | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   2 | Remove the last letter from each word in this text: "{InputText}"                                                  | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   3 | Remove all punctuation from the following text: "{InputText}"                                                      | 🟢                 | 🔴       | 🔴                 | 🔴         |
|   4 | Remove all spaces in this text: "{InputText}"                                                                      | 🔴                 | 🟢       | 🔴                 | 🟢         |
|   5 | Replace all instances of the character '{Char1}' in the following text with '{Char2}': "{InputText}"               | 🟢                 | 🔴       | 🔴                 | 🔴         |
|   6 | Replace all consonants in the following text with asterisks (*): "{InputText}"                                     | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   7 | Replace all spaces in the following text with underscores: "{InputText}"                                           | 🟢                 | 🟢       | 🟢                 | 🟢         |
|   8 | Replace all vowels in the following text with asterisks (*): "{InputText}"                                         | 🟢                 | 🔴       | 🔴                 | 🔴         |
|   9 | Reverse the character order in every third word of the following text, starting with the first word: "{InputText}" | 🔴                 | 🔴       | 🔴                 | 🔴         |
|  10 | Reverse character order in every other word in this text, starting with the first word: "{InputText}"              | 🔴                 | 🔴       | 🔴                 | 🔴         |
|  11 | Swap the case of all letters in the following text: "{InputText}"                                                  | 🟢                 | 🟢       | 🔴                 | 🟢         |

## Composite Transformations

|   # | instruction                                                                                                                            | claude_2_1_cedar   | beaver   | llama_2_70b_chat   | capybara   |
|----:|:---------------------------------------------------------------------------------------------------------------------------------------|:-------------------|:---------|:-------------------|:-----------|
|   1 | Change each letter to alternate case starting with lowercase, shuffle the words, and then reverse the string: "{InputText}"            | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   2 | Double each letter in the text and then reverse the entire string: "{InputText}"                                                       | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   3 | Encode each word in the text as its ASCII value, separated by dashes, then reverse the order of these codes: "{InputText}"             | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   4 | Extract the initials of each word, concatenate them, and reverse the string: "{InputText}"                                             | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   5 | For each word in the text, interleave it with its reverse and then reverse the entire sentence order: "{InputText}"                    | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   6 | Remove all but the first and last word of each sentence, then reverse the order of the remaining sentences in this text: "{InputText}" | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   7 | Remove all but the first letter of each word, then reverse the order of the words in this text: "{InputText}"                          | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   8 | Remove all but the last letter of each word, then reverse the resulting string: "{InputText}"                                          | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   9 | Remove all vowels from the text, duplicate the remaining consonants, and then reverse the string: "{InputText}"                        | 🔴                 | 🔴       | 🔴                 | 🔴         |
|  10 | Replace each word in this text with its length, then reverse the resulting string: "{InputText}"                                       | 🔴                 | 🔴       | 🔴                 | 🔴         |
|  11 | Reverse the order of words and remove all spaces in this text: "{InputText}"                                                           | 🔴                 | 🔴       | 🔴                 | 🔴         |
|  12 | Scramble the inner letters of each word, leaving the first and last letters intact, then reverse the order of the words: "{InputText}" | 🔴                 | 🔴       | 🔴                 | 🔴         |

## Language Understanding

|   # | instruction                                                                                                                                                                                         | claude_2_1_cedar   | beaver   | llama_2_70b_chat   | capybara   |
|----:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|:---------|:-------------------|:-----------|
|   1 | Add commas back into the following text at appropriate places: "{ModifiedText}"                                                                                                                     | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   2 | Vowels have been removed from the following text: "{ModifiedText}". Add back the dropped vowels to restore the complete sentence.                                                                   | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   3 | Add spaces back into the following text where they are missing: "{ModifiedText}"                                                                                                                    | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   4 | All question marks are removed from the following: "{ModifiedText}". Put them back into the text.                                                                                                   | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   5 | The words in the following text have been merged into a single block without spaces: "{ModifiedText}". Separate them back into the original sentence.                                               | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   6 | One character in this text has been changed to another character. Identify the change and reconstruct the original sentence: "{ModifiedText}"                                                       | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   7 | Reorder the words in the following text to form coherent sentences: "{ModifiedText}"                                                                                                                | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   8 | All instances of the letter '{Char1}' have been removed from the following text: "{ModifiedText}". Restore the complete sentence by inserting the letter '{Char1}' back into the correct positions. | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   9 | Punctuation has been removed from the following text: "{ModifiedText}". Add the punctuation back into the text where it belongs.                                                                    | 🔴                 | 🔴       | 🔴                 | 🔴         |
|  10 | A word in the following sentence is scrambled: "{ModifiedText}". Identify the scrambled word, unscramble it, and provide the correct sentence.                                                      | 🔴                 | 🔴       | 🔴                 | 🔴         |
|  11 | Reorder the following scrambled words to form coherent sentences: "{ModifiedText}"                                                                                                                  | 🔴                 | 🔴       | 🔴                 | 🔴         |

## Letter Analysis

|   # | instruction                                                                                                                                                              | claude_2_1_cedar   | beaver   | llama_2_70b_chat   | capybara   |
|----:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|:---------|:-------------------|:-----------|
|   1 | Add a number in parentheses after each word in this text indicating its position: "{InputText}"                                                                          | 🔴                 | 🟢       | 🔴                 | 🔴         |
|   2 | Count the number of consonants in the following text: "{InputText}"                                                                                                      | 🟢                 | 🔴       | 🔴                 | 🔴         |
|   3 | Count the number of lowercase letters in the following text: "{InputText}"                                                                                               | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   4 | Count the number of unique letters in the following text. Exclude numbers and special characters: "{InputText}"                                                          | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   5 | Count the number of uppercase letters in the following text: "{InputText}"                                                                                               | 🟢                 | 🔴       | 🔴                 | 🔴         |
|   6 | Count the number of vowels in the following text: "{InputText}"                                                                                                          | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   7 | Identify all unique letters used in the following text: "{InputText}"                                                                                                    | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   8 | Identify the first letter in the following text that does not repeat. If all letters repeat, return an empty response: "{InputText}"                                     | 🔴                 | 🟢       | 🔴                 | 🟢         |
|   9 | Find the last letter that appears more than once in the following text. If no letter repeats, return an empty response: "{InputText}"                                    | 🔴                 | 🔴       | 🔴                 | 🔴         |
|  10 | Find the first letter that appears exactly 3 times in the following text. Provide the letter. If no letter meets this condition, return an empty response: "{InputText}" | 🔴                 | 🔴       | 🔴                 | 🔴         |
|  11 | Find how many letters appear exactly 3 times in the following text. Provide the count: "{InputText}"                                                                     | 🔴                 | 🔴       | 🔴                 | 🔴         |

## Sentence Manipulation

|   # | instruction                                                                                                                                  | claude_2_1_cedar   | beaver   | llama_2_70b_chat   | capybara   |
|----:|:---------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|:---------|:-------------------|:-----------|
|   1 | Add the word 'Note:' to the beginning of each sentence in the following text: "{InputText}"                                                  | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   2 | Alternate the case of letters in each sentence starting with uppercase for the first sentence and so on in the following text: "{InputText}" | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   3 | Concatenate all sentences in reverse order into one continuous text in the following text: "{InputText}"                                     | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   4 | Number each sentence sequentially starting with 1 in the following text: "{InputText}"                                                       | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   5 | Remove the first and last word from each sentence in this text: "{InputText}"                                                                | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   6 | Remove the second and second-to-last word from each sentence in this text: "{InputText}"                                                     | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   7 | Remove all sentences with 3 words or fewer and 10 words or more from the following text: "{InputText}"                                       | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   8 | Reverse the order of characters in each sentence of the following text, while keeping the original sentence order: "{InputText}"             | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   9 | Reverse the order of sentences in the following text: "{InputText}"                                                                          | 🟢                 | 🔴       | 🔴                 | 🔴         |
|  10 | Reverse the word order in each sentence of the following text, while keeping the original sentence order: "{InputText}"                      | 🔴                 | 🔴       | 🔴                 | 🔴         |
|  11 | Sort all the sentences in the following text by their length, from shortest to longest: "{InputText}"                                        | 🔴                 | 🔴       | 🔴                 | 🔴         |

## Text Analysis

|   # | instruction                                                                                           | claude_2_1_cedar   | beaver   | llama_2_70b_chat   | capybara   |
|----:|:------------------------------------------------------------------------------------------------------|:-------------------|:---------|:-------------------|:-----------|
|   1 | Count the number of words in this text: "{InputText}"                                                 | 🟢                 | 🔴       | 🔴                 | 🔴         |
|   2 | Remove all words with 7 letters or more from the following text: "{InputText}"                        | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   3 | Remove all words with 3 letters or fewer and 7 letters or more from the following text: "{InputText}" | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   4 | Remove all words with 3 letters or fewer from the following text: "{InputText}"                       | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   5 | Remove all words with odd length from this text: "{InputText}"                                        | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   6 | Replace each word with its index in the sentence in this text: "{InputText}"                          | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   7 | Replace each word with its last two letters in this text: "{InputText}"                               | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   8 | Replace each word with its length in this text: "{InputText}"                                         | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   9 | Sort all the words in the following text alphabetically: "{InputText}"                                | 🔴                 | 🔴       | 🔴                 | 🔴         |
|  10 | Sort all the words in the following text by their length, from shortest to longest: "{InputText}"     | 🔴                 | 🔴       | 🔴                 | 🔴         |
|  11 | Sort all the words in the following text by their number of vowels, from least to most: "{InputText}" | 🔴                 | 🔴       | 🔴                 | 🔴         |

## Text Extraction

|   # | instruction                                                                                            | claude_2_1_cedar   | beaver   | llama_2_70b_chat   | capybara   |
|----:|:-------------------------------------------------------------------------------------------------------|:-------------------|:---------|:-------------------|:-----------|
|   1 | Extract all consonants from the following text: "{InputText}"                                          | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   2 | Extract the first word from each sentence in the following text: "{InputText}"                         | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   3 | Extract all unique words from the following text, disregarding case: "{InputText}"                     | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   4 | Extract all vowels from the following text: "{InputText}"                                              | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   5 | Identify all words in this text that contain the letter '{Char1}': "{InputText}"                       | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   6 | Find all words in this text that end with the letter '{Char1}': "{InputText}"                          | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   7 | Extract all words in this text that are longer than 5 letters: "{InputText}"                           | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   8 | Extract all words from the following text where the first and last letters are the same: "{InputText}" | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   9 | Extract all words from the following text that start with a vowel: "{InputText}"                       | 🔴                 | 🔴       | 🔴                 | 🔴         |
|  10 | Extract all words from the following text that have an even number of characters: "{InputText}"        | 🔴                 | 🔴       | 🔴                 | 🔴         |
|  11 | Extract all words in this text that do not contain the letter '{Char1}': "{InputText}"                 | 🔴                 | 🔴       | 🔴                 | 🔴         |

## Text Formatting

|   # | instruction                                                                                                                    | claude_2_1_cedar   | beaver   | llama_2_70b_chat   | capybara   |
|----:|:-------------------------------------------------------------------------------------------------------------------------------|:-------------------|:---------|:-------------------|:-----------|
|   1 | Create an acronym from the following text by taking the first letter of each word and capitalizing it: "{InputText}"           | 🟢                 | 🔴       | 🔴                 | 🔴         |
|   2 | Make every fourth word bold in this text by using Markdown syntax: "{InputText}"                                               | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   3 | Capitalize all words in this text: "{InputText}"                                                                               | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   4 | Capitalize every fourth word in this text, starting with the first word: "{InputText}"                                         | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   5 | Capitalize every other word in this text, starting with the first word: "{InputText}"                                          | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   6 | Convert this text to camel case: "{InputText}"                                                                                 | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   7 | Convert every third word to inline code in Markdown in this text: "{InputText}"                                                | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   8 | Create a Markdown bullet list, where each item is a sentence from the following text: "{InputText}"                            | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   9 | Italicize and bold alternate words in this text using Markdown syntax, starting with italicizing the first word: "{InputText}" | 🔴                 | 🔴       | 🔴                 | 🔴         |
|  10 | Italicize every third word in this text by using Markdown syntax: "{InputText}"                                                | 🔴                 | 🔴       | 🔴                 | 🔴         |
|  11 | Strike through every fifth word in this text by using Markdown syntax: "{InputText}"                                           | 🔴                 | 🔴       | 🔴                 | 🔴         |

## Word Manipulation

|   # | instruction                                                                                   | claude_2_1_cedar   | beaver   | llama_2_70b_chat   | capybara   |
|----:|:----------------------------------------------------------------------------------------------|:-------------------|:---------|:-------------------|:-----------|
|   1 | Alternate the casing of words in this text, starting with lowercase: "{InputText}"            | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   2 | Capitalize every third word in this text, starting with the first word: "{InputText}"         | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   3 | Double each word in the following text: "{InputText}"                                         | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   4 | Double every vowel in the following text: "{InputText}"                                       | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   5 | Remove all but the first and last word from this text: "{InputText}"                          | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   6 | Remove every other word from the following text, starting with the second word: "{InputText}" | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   7 | Remove all words containing '{Char1}' from this text: "{InputText}"                           | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   8 | Remove all words that are shorter than 4 letters in this text: "{InputText}"                  | 🔴                 | 🔴       | 🔴                 | 🔴         |
|   9 | Replace all vowels in the following text with asterisks: "{InputText}"                        | 🟢                 | 🔴       | 🔴                 | 🔴         |
|  10 | Reverse the letters of each word in the following text: "{InputText}"                         | 🟢                 | 🟢       | 🔴                 | 🟢         |
|  11 | Reverse the order of letters in every second word in this text: "{InputText}"                 | 🔴                 | 🔴       | 🔴                 | 🔴         |

