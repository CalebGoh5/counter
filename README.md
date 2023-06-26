# counter
这段代码实现了一个简单的单词计数器，可以统计给定文本中每个单词出现的次数。程序首先使用正则表达式 re.findall() 提取文本中的单词，并将它们转换为小写。然后，使用 collections.Counter() 统计每个单词的出现次数，并将结果存储在 word_counts 中。最后，程序打印出每个单词及其对应的出现次数。

在示例中，我们首先让用户输入要统计的文本。然后，调用 word_counter 函数对文本进行处理，得到单词的出现次数。最后，使用循环打印出每个单词及其出现次数。

请注意，这个示例仅用于演示目的，并没有涉及到更复杂的文本处理技术，比如分词和停用词过滤。在实际应用中，你可能需要更多的文本处理步骤来提高计数器的准确性和性能。此示例仅用于演示基本的单词计数功能。
