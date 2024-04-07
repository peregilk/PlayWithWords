[View extended tasks](./tasks_extended.md)

## Artificial Languages

| instruction                                                                                                 | target         |
|:------------------------------------------------------------------------------------------------------------|:---------------|
| Please convert this text to leetspeak: "{InputText}"                                                        | {ModifiedText} |
| Please convert this text to pig latin: "{InputText}"                                                        | {ModifiedText} |
| Please translate the following text into Igpay Atinlay (Pig Latin with 'ay' after each word): "{InputText}" | {ModifiedText} |

## Character Replacement

| instruction                                                                                             | target         |
|:--------------------------------------------------------------------------------------------------------|:---------------|
| Please remove all punctuation from the following text: "{InputText}"                                    | {ModifiedText} |
| Please remove all spaces in this text: "{InputText}"                                                    | {ModifiedText} |
| Please replace all instances of the letter 'e' in the following text with the number '3': "{InputText}" | {ModifiedText} |
| Please replace all consonants in the following text with asterisks (*): "{InputText}"                   | {ModifiedText} |
| Please replace all punctuation with spaces in this text: "{InputText}"                                  | {ModifiedText} |
| Please replace all spaces in the following text with underscores: "{InputText}"                         | {ModifiedText} |
| Please replace all vowels in the following text with asterisks (*): "{InputText}"                       | {ModifiedText} |

## Character Shuffling

| instruction                                                                                                                             | target         |
|:----------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| Please remove all but the last letter of each word, then reverse the resulting string: "{InputText}"                                    | {ModifiedText} |
| Please remove all but the middle character of each word, then reverse the order of the remaining characters in this text: "{InputText}" | {ModifiedText} |
| Please reverse the order of words and remove all spaces in this text: "{InputText}"                                                     | {ModifiedText} |
| Please swap the case of all letters in the following text: "{InputText}"                                                                | {ModifiedText} |

## Sentence Manipulation

| instruction                                                                                                                                   | target         |
|:----------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| Please reorder the words in the following text to form coherent sentences: "{ModifiedText}"                                                   | {InputText}    |
| Please remove all but the first and last word from this text: "{InputText}"                                                                   | {ModifiedText} |
| Please remove all but the first and last word of each sentence, then reverse the order of the remaining sentences in this text: "{InputText}" | {ModifiedText} |
| Please remove the first and last word from each sentence in this text: "{InputText}"                                                          | {ModifiedText} |
| Please remove the second and second-to-last word from each sentence in this text: "{InputText}"                                               | {ModifiedText} |
| Please remove all sentences with 3 words or fewer and 10 words or more from the following text: "{InputText}"                                 | {ModifiedText} |
| Please reverse the order of characters in each sentence of the following text, while keeping the original sentence order: "{InputText}"       | {ModifiedText} |
| Please reverse the order of sentences in the following text: "{InputText}"                                                                    | {ModifiedText} |
| Please reverse the word order in each sentence of the following text, while keeping the original sentence order: "{InputText}"                | {ModifiedText} |
| Please reverse the word order in the first and last sentence of the following text: "{InputText}"                                             | {ModifiedText} |
| Please sort all the sentences in the following text by their length, from shortest to longest: "{InputText}"                                  | {ModifiedText} |
| Please reorder the following scrambled words to form coherent sentences: "{ModifiedText}"                                                     | {InputText}    |

## Text Analysis

| instruction                                                                         | target         |
|:------------------------------------------------------------------------------------|:---------------|
| Please count the number of words in this text: "{InputText}"                        | {ModifiedText} |
| Please remove all but the first letter of each word in this text: "{InputText}"     | {ModifiedText} |
| Please remove all but the last letter of each word in this text: "{InputText}"      | {ModifiedText} |
| Please remove all but the middle letter of each word in this text: "{InputText}"    | {ModifiedText} |
| Please replace each word with its first letter in this text: "{InputText}"          | {ModifiedText} |
| Please replace each word with its first two letters in this text: "{InputText}"     | {ModifiedText} |
| Please replace each word with its index in the sentence in this text: "{InputText}" | {ModifiedText} |
| Please replace each word with its last two letters in this text: "{InputText}"      | {ModifiedText} |
| Please replace each word with its length in this text: "{InputText}"                | {ModifiedText} |
| Please replace each word with its second letter in this text: "{InputText}"         | {ModifiedText} |

## Text Encoding

| instruction                                                                                    | target         |
|:-----------------------------------------------------------------------------------------------|:---------------|
| Please apply a Caesar cipher with a shift of 5 to the following text: "{InputText}"            | {ModifiedText} |
| Please convert the following text to binary, with spaces between each byte: "{InputText}"      | {ModifiedText} |
| Please convert the following text to hexadecimal, with spaces between each byte: "{InputText}" | {ModifiedText} |

## Text Extraction

| instruction                                                          | target         |
|:---------------------------------------------------------------------|:---------------|
| Please extract all consonants from the following text: "{InputText}" | {ModifiedText} |
| Please extract all vowels from the following text: "{InputText}"     | {ModifiedText} |

## Text Formatting

| instruction                                                                                                                 | target         |
|:----------------------------------------------------------------------------------------------------------------------------|:---------------|
| Please create an acronym from the following text by taking the first letter of each word and capitalizing it: "{InputText}" | {ModifiedText} |
| Please add commas back into the following text at appropriate places: "{ModifiedText}"                                      | {InputText}    |
| Please add spaces back into the following text where they are missing: "{ModifiedText}"                                     | {InputText}    |
| Please add a number in parentheses after each word in this text indicating its position: "{InputText}"                      | {ModifiedText} |
| Please capitalize all words in this text: "{InputText}"                                                                     | {ModifiedText} |
| Please capitalize every fourth word in this text, starting with the first word: "{InputText}"                               | {ModifiedText} |
| Please capitalize every other word in this text, starting with the first word: "{InputText}"                                | {ModifiedText} |
| Please convert this text to camel case: "{InputText}"                                                                       | {ModifiedText} |
| Please convert this text to uppercase: "{InputText}"                                                                        | {ModifiedText} |

## Text Restoration

| instruction                                                                                                                                                                                    | target      |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| Vowels have been removed from the following text: "{ModifiedText}". Please add back the dropped vowels to restore the complete sentence.                                                       | {InputText} |
| The words in the following text have been merged into a single block without spaces: "{ModifiedText}". Please separate them back into the original sentence.                                   | {InputText} |
| The word 'the' has been removed from the following text: "{ModifiedText}". Please reinsert 'the' back into the correct positions to restore the complete sentence.                             | {InputText} |
| All instances of the letter 'e' have been removed from the following text: "{ModifiedText}". Please restore the complete sentence by inserting the letter 'e' back into the correct positions. | {InputText} |
| Punctuation has been removed from the following text: "{ModifiedText}". Please add the punctuation back into the text where it belongs.                                                        | {InputText} |

## Word Manipulation

| instruction                                                                                                                                           | target         |
|:------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| Please double each word in the following text: "{InputText}"                                                                                          | {ModifiedText} |
| Please create portmanteau words from the following text by combining the first half of each word with the second half of the next word: "{InputText}" | {ModifiedText} |
| Please remove all but the first and last character of each word in this text: "{InputText}"                                                           | {ModifiedText} |
| Please remove all but the first letter of each word, then reverse the order of the words in this text: "{InputText}"                                  | {ModifiedText} |
| Please remove duplicate words from this text: "{InputText}"                                                                                           | {ModifiedText} |
| Please remove every other word from the following text, starting with the second word: "{InputText}"                                                  | {ModifiedText} |
| Please remove every second and third word from the following text, starting with the second word: "{InputText}"                                       | {ModifiedText} |
| Please remove the last letter from each word in this text: "{InputText}"                                                                              | {ModifiedText} |
| Please remove all words with 7 letters or more from the following text: "{InputText}"                                                                 | {ModifiedText} |
| Please remove all words with 3 letters or fewer and 7 letters or more from the following text: "{InputText}"                                          | {ModifiedText} |
| Please remove all words with 3 letters or fewer from the following text: "{InputText}"                                                                | {ModifiedText} |
| Please remove all words containing 'a' from this text: "{InputText}"                                                                                  | {ModifiedText} |
| Please remove all words with odd length from this text: "{InputText}"                                                                                 | {ModifiedText} |
| Please replace each word in this text with its length, then reverse the resulting string: "{InputText}"                                               | {ModifiedText} |
| Please replace each word with its palindrome in this text: "{InputText}"                                                                              | {ModifiedText} |
| Please reverse the character order in every fifth word of the following text, starting with the first word: "{InputText}"                             | {ModifiedText} |
| Please reverse the character order in every third word of the following text, starting with the first word: "{InputText}"                             | {ModifiedText} |
| Please reverse each word in this text: "{InputText}"                                                                                                  | {ModifiedText} |
| Please reverse every other word in this text, starting with the first word: "{InputText}"                                                             | {ModifiedText} |
| Please reverse every third word in this text, starting with the first word: "{InputText}"                                                             | {ModifiedText} |
| Please sort all the words in the following text alphabetically: "{InputText}"                                                                         | {ModifiedText} |
| Please sort all the words in the following text by their length, from shortest to longest: "{InputText}"                                              | {ModifiedText} |
| Please sort all the words in the following text by their number of vowels, from least to most: "{InputText}"                                          | {ModifiedText} |
| A word in the following sentence is scrambled: "{ModifiedText}". Please identify the scrambled word, unscramble it, and provide the correct sentence. | {InputText}    |
