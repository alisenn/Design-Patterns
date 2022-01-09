class President:
    def __init__(self):
        pass

    def listen_problem(self) -> None:
        pass

    def give_money(self) -> None:
        pass


class RealPresident(President):
    def listen_problem(self) -> None:
        print("President: I am listening.")

    def give_money(self) -> None:
        print("President: I won't give you money.")


class ProxyPresident(President):
    def __init__(self, real_subject: RealPresident) -> None:
        super().__init__()
        self.real_president = real_president

    def listen_problem(self) -> None:
        print("Proxy: I am listening.")
        self.real_president.listen_problem()

    def give_money(self) -> None:
        print("Proxy: I won't give you money.")

print("Someone want to talk with president")
real_president = RealPresident()
proxy_president = ProxyPresident(real_president)

proxy_president.listen_problem()
proxy_president.give_money()