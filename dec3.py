  def upper_decorator(func):
        def wrapper():
            data = func().upper()
            return data

        return wrapper

  def split_decorator(func):
      def wrapper():
          data = list(func())
          return data
      return wrapper


    @split_decorator
    def my_name_func():
        return 'Ramin'


    if __name__ == '__main__':
        name = my_name_func()
        print(name)