-- CptS 355 - Lab 1 (Haskell) - Spring 2021
-- Name: Joseph Steeb
-- Collaborated with: 

--import Data.List

module Lab1
    where

import System.IO
import System.Directory.Internal.Prelude (Num)
import Data.List (isSubsequenceOf)
--import GHC.Tuple

-- 1.insert

getFirst :: (a, b) -> a
getFirst (a,b) = a
getSecond :: (a, b) -> b
getSecond (a,b) = b

append :: Int -> a -> [a] -> [a]
append index number list = number : getSecond (splitAt index list)
     
insert index number list
    |index > length list = list
    |otherwise = getFirst (splitAt index list) ++ append index number list

-- 2. insertEvery


insertEveryHelper :: Int -> Int -> a -> [a] -> Int -> [a]
insertEveryHelper index step item list lengthl
    |lengthl < index = list
    |lengthl >= index + step = insertEveryHelper (index + step + 1) step item (insert index item list) (lengthl + 1)
    |lengthl >= index = insert index item list
    |otherwise = []


insertEvery :: Int -> a -> [a] -> [a]
insertEvery number item list = insertEveryHelper number number item list (length list)

-- 3. getSales

getSalesHelper day list index count
    |index == length list = count
    |isSubsequenceOf (fst (list !! index)) day = getSalesHelper day list (index+1) (count + snd (list!!index))
    |index < length list = getSalesHelper day list (index+1) count
    |otherwise = count

getSales :: String -> [(String, Integer)] -> Integer
getSales day list = getSalesHelper day list 0 0

-- 4. sumSales

-- 5. split


-- 6. nSplit

