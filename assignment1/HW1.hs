-- CptS 355 - Fall 2021 -- Homework1 - Haskell
-- Name: Joseph Steeb
-- Collaborators: None

module HW1
     where

-- Q1 everyOther
everyOther list = removeOther False (length list) list
     where
          removeOther isOdd n [] = []
          removeOther isOdd 0 (x:xs) = xs
          removeOther isOdd n (x:xs)
               | isOdd = removeOther (not isOdd)(n-1) xs
               | otherwise = x:(removeOther (not isOdd) (n-1) xs)

-- Q2(a) eliminateDuplicates

eliminateDuplicates list = elimDupHelp 0 list [] 
     where
          elimDupHelp 0 [] [] = []
          elimDupHelp index list list2
               | index > (length list)-1 = list2
               | elem (list !! index) list2 = elimDupHelp (index+1) list list2
               | not (elem (list !! index) list2) = elimDupHelp (index+1) list ((list !! index) : list2)
               | otherwise = []

-- Q2(b) matchingSeconds
matchingSeconds :: Eq t => t -> [(t, a)] -> [a]
matchingSeconds name list = matchingSecondsHelp name list []
     where    
     matchingSecondsHelp name [] rList = rList
     matchingSecondsHelp name (x:xs) rList
          | fst x == name = matchingSecondsHelp name xs (snd x:rList)
          | otherwise = matchingSecondsHelp name xs rList

-- Q2(c) clusterCommon
clusterCommon :: (Eq t, Eq a) => [(t, a)] -> [(t, [a])]
clusterCommon [] = []
clusterCommon (x:xs) = (fst x, matchingSeconds (fst x) (x:xs)) : clusterCommon (removeN (fst x) xs)
     where
          removeN name [] = []
          removeN name (x:xs)
               | fst x == name = removeN name xs
               | otherwise = x:removeN name xs

-- Q3 maxNumCases
maxNumCases :: (Num p, Ord p, Eq t) => [(a, [(t, p)])] -> t -> p
maxNumCases list month = maxNumCasesHelp 0 list month
     where
          maxNumCasesHelp max [] month = max
          maxNumCasesHelp  max (x:xs) month
               | sum (matchingSeconds month (snd x)) > max = maxNumCasesHelp (sum (matchingSeconds month (snd x))) xs month
               | otherwise = maxNumCasesHelp max xs month

-- Q4 groupIntoLists
--gets a substring inbetween two indices


groupIntoLists :: [a] -> [[a]]
groupIntoLists list = groupIntoListsHelp 0 1 2 list
     where
          getMiddle index1 index2 list = drop index1 (reverse (drop (length list - index2) (reverse list)))
          groupIntoListsHelp index1 index2  acc list
               | null list = []
               | index2 >= length list = [getMiddle index1 (length list) list]
               | otherwise = [getMiddle index1 index2 list] ++ groupIntoListsHelp index2 (index2+acc) (acc+1) list

-- Q5 getSlice 
getSlice :: Eq a => (a, a) -> [a] -> [a]
getSlice chars list = getSliceHelp chars list [] False
     where
          getSliceHelp chars [] rList flag = rList
          getSliceHelp chars (x:xs) rList flag
               | x == fst chars && not flag = getSliceHelp chars xs rList True
               | flag && x == snd chars =  rList
               | flag = getSliceHelp chars xs (rList++[x]) flag
               | otherwise = getSliceHelp chars xs rList flag


