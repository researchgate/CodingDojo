class Fixnum
	def happy?
    if self**2 < 10
      return self == 1
    end
    self.to_s.split(//).map{|n| n.to_i ** 2}.inject(:+).happy?
  end
end
