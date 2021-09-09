# Python Kotlin Runner
A [`kotlin`](https://kotlinlang.org) file runner I wrote in [`Python`](https://python.org) for running kotlin files in Windows [Geany 1.37.1](https://github.com/geany/geany/releases/tag/1.37.1) because<br>despite the tutorials and closed issue on [Geany](https://github.com/geany/geany/issues/1581#issuecomment-405182480) for the same, I was not able to get a working<br>solution.

<hr>

## You need [kotlinc](https://github.com/JetBrains/kotlin/releases/tag/v1.2.21) and [JDK8]()

<ul>
  <li>Copy the extracted kotlinc to any directory</li>
  <li>To be on the safer side, add the bin path to both system and user ENVs<br>Eg. - If you extracted the zip to <b>C:\Program Files</b> the path required will<br>be <b>C:\Program Files\kotlinc\bin</b></li>
  <li>Save the kotlin file before running</li>
  <li>Run <b>this.py</b> in the same directory of the file you want to run</li>
  <ul>
    <li>Enter the file index according to the list in terminal</li>
    <li>Output will be in <i>lime</i> colour</li>
    <li>Press <b>ENTER</b> to exit</li>
  </ul>
</ul>

<hr>

## This can be extended further with a while loop if<br>you want to run until you don't want to quit.
## And even further with `threading` if you want to run<br>multiple kotlin files at once.
