#include <iostream>

class Element {
  public:
  std::string get_name() const {return name;}
  double get_mass() const {return mass;}
  void set_name(std::string new_name) {name = new_name;}
  void set_mass(double new_mass) {mass = new_mass;}
  void read() const;

  private:
  std::string name;
  double mass;
};

void Element::read() const {
  std::cin >> name;
  std::cin >> mass;
}

std::vector<string> split(std::string str) {
  int start = 0;
  for (unsigned i = 0; i < str.std::size(); i++) {
    start = 
    if (str[i] == ' ') {
      
    }
  }
}

int main () {

  return 0;
}