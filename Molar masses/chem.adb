with Ada.Text_IO; use Ada.Text_IO;

procedure main is
    -- Define a type Element which has two parts:
    -- a molar mass and an element name
    type Element is record
        Name : String(1..2); -- can have one or two chars
        Mass : Float;
    end record;
    
    Hydrogen : constant Element := ("H ", 1.00784);
    Helium : constant Element := ("He", 4.0026);
    Lithium : constant Element := ("Li", 6.941);
    Beryllium : constant Element := ("Be", 9.0121);
    
    Elements : constant array(1..4) of Element := (Hydrogen, Helium, Lithium, Beryllium);
    Total_Mass : Float := 0.0;
    -- Formula : String := "";
begin 
    -- Graphical perodic table
    Put_Line("  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18");
    Put_Line("1 H                                                  He");
    Put_Line("2 Li Be                               B  C  N  O  F  Ne");
    Put_Line("3 Na Mg                               Al Si P  S  Cl Ar");
    Put_Line("4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr");
    Put_Line("5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe");
    Put_Line("6 Cs Ba    Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn");
    Put_Line("7 Fr Ra    Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og");
    Put_Line("8 Uue Ubn");
    New_Line;
    Put_Line("        La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu");
    Put_Line("        Ac Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr");
    Put_Line("        Ubu Ubb Ubt Ubq Ubp Ubh Ubs");
    
    -- Take input for the chemical formula and count molar masses
    New_Line;
    Put_Line("Enter a simple chemical formula (no parentheses or coefficents for this version)");
    
    declare
        Formula : String := get_line; -- Gets line of input
    begin
        for i in 1 .. 4 loop -- Loop over the array of Elements
            for j in 1 .. Formula'Length loop -- Loop over the input
                if j + 1 <= Formula'Length then -- Ensure that the following splice is in range
                    if Formula(j..j+1) = Elements(i).name then
                        Total_Mass := Total_Mass + Elements(i).Mass;
                        -- Put_Line("Current array is: " & Float'Image(Elements(i).Mass));
                    end if;
                end if;
            end loop;
            New_Line;
        end loop;
        -- or Formula(j..j+1) = Elements(i).Name(1)
 
        Put_Line("The molar mass of " & Formula & " is " & loat'Image(Total_Mass));
    end;
end main;


-- function (g_mol : Float)

-- procedure Hello is
-- begin
--   Put_Line("Hello, world!");
-- end Hello;

-- procedure main is 
--     input : Integer;
-- begin 
--     Ada.Text_IO.Put ("Enter an element and the number atoms contained in the compound. Enter 0 to quit.");
--     Ada.Integer_Text_IO.Get(I);
--     while input != 0:
--         Ada.Text_IO.Put ("Enter an integer: ");
--         Ada.Integer_Text_IO.Get(I);
-- end main;
