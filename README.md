# Pseudonymization Techniques in Python

This presentation is from a talk I gave at [Boulder Python](https://www.boulderpython.org) in June 2018 ([event link](https://www.meetup.com/BoulderPython/events/249980711/)).

To see the presentation, visit: [frankv.github.io/pseudonymization-in-python_BoulderPython_0618/](https://frankv.github.io/pseudonymization-in-python_BoulderPython_0618/)


## Abstract
Protecting user data has always been an important task, but now thanks to GDPR, it's the law! Join Boulder Python's co-organizer Frank for a discussion on data protection using a technique known as pseudonymization. If you're concerned about best practices for protecting user identities in your apps, you don't want to miss this talk!


## Outline
1. What is pseudonymization?
	- _Pseudonymization is a data de-identification procedure._
2. Why would you do this?
	- protect user identities
	- secure a dataset from identification
	- 🚨 GDPR 🚨
3. GDPR from 10,000 feet
	- <blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">&quot;I am not a lawyer, I will not answer your legal questions.&quot; - <a href="https://twitter.com/fmdfrank?ref_src=twsrc%5Etfw">@fmdfrank</a></p>&mdash; BoulderPython (@BoulderPython) <a href="https://twitter.com/BoulderPython/status/1006702079778291714?ref_src=twsrc%5Etfw">June 13, 2018</a></blockquote>
	- What is GDPR?
	- The Rules
	- What is Personal Data w/ Examples
4. Who does this effect?
5. "The Long Arm of the Law"
6. Data Privacy Techniques
	- Pseudonymization
	- Anonymization
7. Pseudonymization Techniques
	- Data Masking
	- Approximation
	- Encryption
	- Tokenization
8.Simple Python Example
	- Class `properties` and `getter`/`setter`
	- A Simple Masking Algorithm
9. Django Example
	- Pseudonymizing a User model w/ `getter`/`setter`
	- Finishing the Job
		- Update QuerySet
		- Pseudonym Exclusion
		- Update `django-admin`
10. Demonstration


## Notes
You can find the example masking algorithm in [examples/simple_masking.py](https://github.com/frankV/pseudonymization-in-python_BoulderPython_0618/blob/master/examples/simple_masking.py)


## Talk Nerdy To Me
- 🐦 [@fmdfrank](https://twitter.com/fmdfrank)
- 📩 frank [at] cuttlesoft [dot] com
- 🐙 [Cuttlesoft](https://cuttlesoft.com)