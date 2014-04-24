require_relative 'happynumbers'

describe Fixnum, "#happy?" do
	it "returns true for 1" do
		1.happy?.should eq (true)
	end

	it "returns false for 2" do
		2.happy?.should eq (false)
	end

	it "returns true for 7" do
		7.happy?.should eq (true)
	end

	it "returns false for 8" do
		8.happy?.should eq (false)
	end

	it "returns true for 10" do
		10.happy?.should eq (true)
	end

	it "returns false for 11" do
		11.happy?.should eq (false)
	end

	it "returns true for 13" do
		13.happy?.should eq (true)
	end

  it "returns true for 998" do
		998.happy?.should eq (true)
	end

  it "returns false for 999" do
		999.happy?.should eq (false)
	end

end
