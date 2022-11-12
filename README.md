This program uses Selenium WebDriver and receives the address of a web page as the input and checks the following rules on that page and finally displays the results (i.e. for each rule, displays each violation of that rule in the form of a proper message in the output):
1. The destination of a link should not directly target images.([explanation](https://rules.sonarsource.com/html/type/Code%20Smell/RSPEC-1092))
2. Deprecated attributes should not be used.([explanation](https://rules.sonarsource.com/html/type/Code%20Smell/RSPEC-1827))
3. META tags should not be used to refresh the page or redirect.([explanation](https://rules.sonarsource.com/html/type/Code%20Smell/RSPEC-1094))
4. The "style" attribute should not be used.([explanation](https://rules.sonarsource.com/html/type/Code%20Smell/RSPEC-1935))
5. Links with identical texts should have identical targets.([explanation](https://rules.sonarsource.com/html/type/Code%20Smell/RSPEC-1101))
6. None of the <input> tags should visually overlap with each other. In the _sample1.htm_ file, the <input> elements overlap. There is no overlaps in the _sample2.htm_ file. To make sure that the selected page follows the rule, this program checks this rule on both Chrome and Firefox browsers and in windows with the following sizes:
[800x600], [1024x768], [1448x1072], [1600x1200], [2048x1536]
