<h1>2740 - Curry</h1><h2>Difficulty: Medium - <a href="https://leetcode.com/problems/curry/">curry</a></h2><p>Given a function&nbsp;<code>fn</code>,&nbsp;return&nbsp;a&nbsp;<strong>curried</strong>&nbsp;version of that function.</p>

<p>A&nbsp;<strong>curried</strong>&nbsp;function is a function that accepts fewer or an equal number of&nbsp;parameters as the original function and returns either another&nbsp;<strong>curried</strong>&nbsp;function or the same value the original function would have returned.</p>

<p>In practical terms, if you called the original function like&nbsp;<code>sum(1,2,3)</code>, you would call the&nbsp;<strong>curried</strong>&nbsp;version like <code>csum(1)(2)(3)<font face="sans-serif, Arial, Verdana, Trebuchet MS">,&nbsp;</font></code><code>csum(1)(2,3)</code>,&nbsp;<code>csum(1,2)(3)</code>, or&nbsp;<code>csum(1,2,3)</code>. All these methods of calling the <strong>curried</strong> function&nbsp;should return the same value as the original.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
fn = function sum(a, b, c) { return a + b + c; }
inputs = [[1],[2],[3]]
<strong>Output:</strong> 6
<strong>Explanation:</strong>
The code being executed is:
const curriedSum = curry(fn);
curriedSum(1)(2)(3) === 6;
curriedSum(1)(2)(3) should return the same value as sum(1, 2, 3).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong>
fn = function sum(a, b, c) { return a + b + c; }
inputs = [[1,2],[3]]
<strong>Output:</strong> 6
<strong>Explanation:</strong>
curriedSum(1, 2)(3) should return the same value as sum(1, 2, 3).</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong>
fn = function sum(a, b, c) { return a + b + c; }
inputs = [[],[],[1,2,3]]
<strong>Output:</strong> 6
<strong>Explanation:</strong>
You should be able to pass the parameters in any way, including all at once or none at all.
curriedSum()()(1, 2, 3) should return the same value as sum(1, 2, 3).
</pre>

<p><strong class="example">Example 4:</strong></p>

<pre>
<strong>Input:</strong>
fn = function life() { return 42; }
inputs = [[]]
<strong>Output:</strong> 42
<strong>Explanation:</strong>
currying a function that accepts zero parameters should effectively do nothing.
curriedLife() === 42
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= inputs.length &lt;= 1000</code></li>
	<li><code>0 &lt;= inputs[i][j] &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= fn.length &lt;= 1000</code></li>
	<li><code>inputs.flat().length == fn.length</code></li>
	<li>function parameters explicitly defined</li>
	<li>If <code>fn.length &gt; 0</code>&nbsp;then the last array in <code>inputs</code> is not empty</li>
	<li>If&nbsp;<code>fn.length === 0</code> then <code>inputs.length === 1</code>&nbsp;</li>
</ul>
