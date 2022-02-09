-- CptS 355 - Lab 2 (Haskell) - Fall 2021
-- Name: Joseph Steeb
-- Collaborated with: 
module Lab2
     where
import GHC.TypeLits (natVal')
merge2H [] [] l3 switch = l3
merge2H l1 [] l3 switch = merge2H (drop 1 l1) [] (l3 ++ [head l1]) switch
merge2H [] l2 l3 switch = merge2H [] (drop 1 l2) (l3 ++ [head l2]) switch
merge2H l1 l2 l3 True = merge2H (drop 1 l1) l2 (l3 ++ [head l1]) False
merge2H l1 l2 l3 False = merge2H l1 (drop 1 l2) (l3 ++ [head l2]) True
-- 1
{- (a) merge2 -}
merge2 :: [a] -> [a] -> [a]
merge2 l1 l2 = merge2H l1 l2 [] True

{- (b) merge2Tail -}
merge2Tail :: [a] -> [a] -> [a]
merge2Tail l1 l2 = merge2H l1 l2 [] True

{- (c) mergeN -}
mergeN list = foldl merge2 [] list

-- 2
{- (a) count -}
count :: Eq a => a -> [a] -> Int
count num arr = length (filter (==num) arr) 


-- 3                
{- (a) concatAll -}
concatAll :: [[String]] -> String
concatAll [[]] = ""
concatAll x = foldr (++) "" (map concat x)



{- (b) concat2Either -}               
data AnEither  = AString String | AnInt Int
                deriving (Show, Read, Eq)

concat2Either:: [[AnEither]] -> AnEither
concat2Either x = foldr concatHelper (AString "") (map (foldr concatHelper (AString "")) x) where
concatHelper :: AnEither -> AnEither -> AnEither
concatHelper (AString x) (AnInt y) = AString(x ++ (show y))
concatHelper (AString x) (AString y) = AString(x ++ y)
concatHelper (AnInt x) (AString y) = AString((show x) ++ y)


-- 4      
{-  concat2Str -}               




data Op = Add | Sub | Mul | Pow
          deriving (Show, Read, Eq)

evaluate:: Op -> Int -> Int -> Int
evaluate Add x y =  x+y
evaluate Sub   x y =  x-y
evaluate Mul x y =  x*y
evaluate Pow x y = x^y

data ExprTree a = ELEAF a | ENODE Op (ExprTree a) (ExprTree a)
                  deriving (Show, Read, Eq)

concat2Str:: [[AnEither]] -> String
concat2Str x = foldr concatHelp "" (foldr (++) [] x) where
concatHelp :: AnEither -> String -> String
concatHelp (AString x) y = (x ++ y)
concatHelp (AnInt x) y = (show(x) ++ y)

-- 5 
{- evaluateTree -}
evaluateTree (ELEAF n) = n
evaluateTree (ENODE Mul e1 e2) = (evaluateTree e1) * (evaluateTree e2)
evaluateTree (ENODE Add e1 e2) = (evaluateTree e1) + (evaluateTree e2)
evaluateTree (ENODE Sub e1 e2) = (evaluateTree e1) - (evaluateTree e2)


-- 6
{- printInfix -}



--7
{- createRTree -}
data ResultTree a  = RLEAF a | RNODE a (ResultTree a) (ResultTree a)
                     deriving (Show, Read, Eq)






