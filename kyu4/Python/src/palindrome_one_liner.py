"""Solution for kata http://www.codewars.com/kata/one-line-task-palindrome-string/."""

palindrome=lambda n,s:(s*n)[:n//2]+(s*n)[~-n//2::-1]
