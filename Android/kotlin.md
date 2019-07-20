The question mark in Kotlin
* [We can add a `?` after the data type of that property which declares that variable as a nullable property.](https://medium.com/@agrawalsuneet/safe-calls-vs-null-checks-in-kotlin-f7c56623ab30)
* [Chinese explanation](https://medium.com/@louis383/kotlin-%E9%80%99%E4%BA%9B%E7%AC%A6%E8%99%9F%E5%88%B0%E5%BA%95%E4%BB%80%E9%BA%BC%E6%84%8F%E6%80%9D-4274d3ae32ab)
* [Official document](https://kotlinlang.org/docs/reference/basic-syntax.html#using-nullable-values-and-checking-for-null)


Remember that if a var is not nullable then you cannot set it to null. For example:
```
val address: String = null
```
Remember that you can use the question mark "?" to declare a variable as null, but you can still set a value to it. For example:
```
val amount: Double? = 10.0
```


Remember that a list in Kotlin can contain null items as well as be null itself. 
```
var list: List<String>? = listof(null, null)
```


Remember that you can check if a variable is equal to null using the equality operator "==" or using the question mark "?" when using it