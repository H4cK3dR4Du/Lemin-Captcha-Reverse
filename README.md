<h1 align="center">✨ 𝕃𝕖𝕞𝕚𝕟 ℂ𝕒𝕡𝕥𝕔𝕙𝕒 ℝ𝕖𝕧𝕖𝕣𝕤𝕖 ✨</h1>

<p align="center">
  <img src="https://img.shields.io/github/stars/H4cK3dR4Du/Lemin-Captcha-Reverse.svg?style=for-the-badge&labelColor=black&color=c1121f&logo=IOTA"/>
  <img src="https://img.shields.io/github/languages/top/H4cK3dR4Du/Lemin-Captcha-Reverse.svg?style=for-the-badge&labelColor=black&color=c1121f&logo=javascript"/>
</p>

<h2 align="center"> 📝 Description 📝 </h2>

<p align="center">
  In this repository, I will explain how <a href="https://www.leminnow.com/">Lemin Captcha</a> works and how they encrypt their payload 'answers' for the captcha. We will analyze code and much more.
</p>

<p align="center">
  <b><big>❤️ Made By H4cK3dR4Du ❤️</big></b>
</p>

<h2 align="center"> 🤷‍♂️ Issues / Doubts 🤷‍♂️</h2>

- **If you have any questions do not hesitate to enter my discord: https://discord.gg/raducord**
- **Or if you have any error do not forget to report it in: [issues](https://github.com/H4cK3dR4Du/Lemin-Captcha-Reverse/issues/new)**

<h2 align="center"> 🚀 Lemin Reverse 🚀 </h2>

### - Requirements And Files:

- **Download Node [here](https://nodejs.org/en/download/package-manager)**
- **Download Python [here](https://www.python.org/downloads/)**

### - Lemin-Captcha-Reverse Documentation:

## Base32

*Base 32 is a positional numeral system that uses 32 as its base. It is similar to the Base64 positional numeral system but uses 32 as its base instead of 64. To represent numbers, it uses the 26 uppercase letters A-Z and the six digits 2-7.*

## Payload

*Lemin captcha to obtain the 'answer' value in its payload /pre-validate concatenates mouse movements (x, y) encoded using Base32 into a list. Finally, they join all the values together with 'x' in between.*

## Info

*When I say mouse movements I mean where you move the puzzle piece, they calculate the top and margin to get the x, and based on your mouse movement.*

## Table With Information

| Name | Type | Method |
|----------|----------|----------|
| _0x54d4ca | Variable | It is the solved token (Ex: gAAAAABmhIX-rBgO-grgtR9x8BPoYEyavVpt-Pg2RBp...) |
| _0x453ccd | Variable | It is a div where they will gradually include the answers by calculating the movement of your mouse (x, y) |
| _0xdd66a7 | Function | It is the function where the 'answer' value is created based on the movements of your mouse |
| _0x569515 | Variable | Variable used to accumulate the value of _0x453ccd.getAttribute('value') until reaching the end |
| _0x5b62e4 | Variable | This variable contains your actual mouse movements (X) |
| _0x1b121f | Variable | This variable contains your actual mouse movements (Y) |
| _0x8a9741 | List | List where they store all your encoded mouse movements in base32 (Ex: ['0', 'a', 'cg', '0', '0', 'cg', '0', '0', 'c6', '']) |
| _0x37f8ea | List | Temporary list where new mouse events are stored (Ex: ['0', 'a', 'cg', '']) |
| _0x16c631 | Function | Function where they join the answer with the solved token once everything is encoded |
| _0x3eee1b | Variable | Variable whose value is 32 since it is used in this way: toString(_0x3eee1b) and means that they are passing it to string using base32 |
| _0x16d00f | Function | Function that is responsible for POST to the Lemin api with the payload built in the variable '_0x3eb0cd' |
| _0x56c799 | Variable | This variable is a 2-parameter json containing 'answers' and 'challenge_id', the 2 obtained from const _0x52f99d = _0x5b87cb() |

## Get Payload

*If you want to get the 'answers' parameter to make your own Lemin solver you must first calculate the pos of the photo and use (x, y) with your mouse as Lemin captcha does. Once that's done you can use my code 'build_payload.py'*

```py
class Variables:
    _0x3eee1b = 32
    _0x29eb83 = ''
    _0x5ae82c = 0
    _0x5b62e4 = 10 # Puzzle Starts at X -> 10
    _0x1b121f = 400 # Puzzle Starts at X -> 400
    _0x272d06 = 'x'
    _0x37f8ea = ['0', 'a', 'cg']
    _0x8a9741 = ['0', 'a', 'cg']
    _0x453ccd = ''
    _0x22bffe = 300
    _0x569515 = ''
    _0x5ab679 = ['1']
    original = ''

class BuildPayload:
    def __init__(self) -> None:
        self.variables = Variables()

    def __encodeMovement__(self, num) -> str:
        chars = '0123456789abcdefghijklmnopqrstuv'
        if num == 0:
            return '0'
        
        base32 = ''

        while num:
            num, i = divmod(num, 32)
            base32 = chars[i] + base32

        return base32
    
    def __buildPayload__(self, x_list, y_list) -> str:
        for x, y in zip(x_list, y_list):
            result = self.variables._0x272d06.join(self.variables._0x8a9741) + self.variables._0x29eb83
            self.variables._0x29eb83 += str(self.variables._0x5ae82c) + self.variables._0x272d06 + str(
                self.variables._0x5b62e4) + self.variables._0x272d06 + str(self.variables._0x1b121f) + self.variables._0x272d06

            if self.variables._0x29eb83 != self.variables._0x272d06.join(self.variables._0x37f8ea):
                self.variables._0x453ccd = self.variables._0x272d06.join(
                    self.variables._0x8a9741) + self.variables._0x29eb83

                self.variables._0x569515 += result
                # print("_0x569515 ->", self.variables._0x569515)

                self._0x8a9741 = self.variables._0x569515.split(self.variables._0x272d06)[-(int(self.variables._0x22bffe)):]
                self._0x37f8ea = self._0x8a9741[-(len(self.variables._0x5ab679) * 3 + 1):]
                
                # print("_0x8a9741 ->", _0x8a9741)
                # print("_0x37f8ea ->", _0x37f8ea)

                x_encoded = self.__encodeMovement__(x)
                y_encoded = self.__encodeMovement__(y)

                # print("Encoded X ->", x_encoded)
                # print("Encoded Y ->", y_encoded)

                self.variables._0x8a9741.extend(['0', x_encoded, y_encoded])

        self.variables.original = self.variables._0x8a9741
    
    def __makePayload__(self) -> str:
        payload = 'x'.join(self.variables.original)
        return payload

if __name__ == "__main__":
    i = BuildPayload()
    x_list = [10, 20, 30, 40, 50, 60, 70]
    y_list = [400, 390, 380, 370, 360, 350, 340, 330, 320]
    i.__buildPayload__(x_list, y_list)
    print("Encoded Mouse Movements _0x8a9741 ->", i.variables.original)
    payload = i.__makePayload__()
    print("Answers Payload ->", payload) 
```

*This code is based on x "moves", and it will build you the payload exactly like Lemin captcha does! You just have to modify it a little and make your own system to calculate the x, y. If you don't know how to do it, give me a tap on my discord and I'll answer you there.*

## Debug

https://github.com/H4cK3dR4Du/Epicgames-Xal/assets/118562174/4a83cf37-1d96-4359-b472-1bb2030d3f58
