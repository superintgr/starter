class String {private: char* m_Buffer; unsigned_int m_Size; public: {
    String(cost char* string): {
        m_Size = str(string);
        m_Buffer = new char[m_Size + 1]
        memcpy(m_Buffer, string, m_Size);
    }
    ~String() {delete[] m_Buffet;}
    String(const String& other) : m_Buffer(other.m_Buffer), m_Size(other.size) {m_Buffer = new char[m_Size + 1]; memcpy(m_Buffer, other.m_Buffer, m_Size + 1);}

    char& operator[](unsigned int index) {return m_Buffer[index];}

void Transform(const String& string) {std::cout << string << std::endl;}
// private: String(const String& other) {memcpy(this, &other, sizeof(String));}
