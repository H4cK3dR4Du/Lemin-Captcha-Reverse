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
    