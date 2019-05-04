#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 12:58:18 2019

@author: yeli
"""

import unittest

class TestGetID(unittest.TestCase): 

    def test1(self):
        self.assertEqual(get_id('000~Jerry-Harrison~No-More-Reruns.txt'), '000')
        
    def test2(self):
        self.assertEqual(get_id('1000~Champian-Fulton~Easy-to-Love.txt'), '1000')

suite1 = unittest.defaultTestLoader.loadTestsFromTestCase(TestGetID)
unittest.TextTestRunner().run(suite1)

class TestGetArtist(unittest.TestCase): 

    def test1(self):
        self.assertEqual(get_artist('000~Jerry-Harrison~No-More-Reruns.txt'), 'Jerry Harrison')
        
    def test2(self):
        self.assertEqual(get_artist('979~Atrocity~Die-Liebe.txt'), 'Atrocity')
        
suite2 = unittest.defaultTestLoader.loadTestsFromTestCase(TestGetArtist)
unittest.TextTestRunner().run(suite2)

class TestGetTitle(unittest.TestCase): 

    def test1(self):
        self.assertEqual(get_title('000~Jerry-Harrison~No-More-Reruns.txt'), 'No More Reruns')
        
    def test2(self):
        self.assertEqual(get_title('840~Big-Maybelle~Candy.txt'), 'Candy')
        
suite3 = unittest.defaultTestLoader.loadTestsFromTestCase(TestGetTitle)
unittest.TextTestRunner().run(suite3)


class TestGetKidSafe(unittest.TestCase): 

    def test1(self):
        l1 = '''Twinkle, twinkle, little star
                How I wonder what you are
                Up above the world so high
                Like a diamond in the sky
                Twinkle, twinkle little star
                How I wonder what you are'''
        self.assertTrue(get_kid_safe(l1) > 0.5)
        
    def test2(self):
        l2 = '''Fuck you (fuck you)
                Fuck you very, very much
                'Cause your words don't translate
                And it's getting quite late
                So, please don't stay in touch'''
        self.assertTrue(get_kid_safe(l2) < 0.5)
        
suite4 = unittest.defaultTestLoader.loadTestsFromTestCase(TestGetKidSafe)
unittest.TextTestRunner().run(suite4)


class TestGetLove(unittest.TestCase): 

    def test1(self):
        l1 = '''Love was when I loved you'''
        self.assertEqual(get_love(l1), 2)
        
        
suite5 = unittest.defaultTestLoader.loadTestsFromTestCase(TestGetLove)
unittest.TextTestRunner().run(suite5)

class TestGetLength(unittest.TestCase): 

    def test1(self):
        l1 = '''Love was when I loved you'''
        self.assertEqual(get_length(l1), 6)
        
        
suite6 = unittest.defaultTestLoader.loadTestsFromTestCase(TestGetLength)
unittest.TextTestRunner().run(suite6)

class TestGetMood(unittest.TestCase): 

    def test1(self):
        l1 = '''It's a beautiful night
                we're looking for something dumb to do
                Hey baby, I think I wanna marry you'''
        self.assertTrue(get_mood(l1) > 0.5)
        
    def test2(self):
        l2 = '''Fuck you (fuck you)
                Fuck you very, very much
                'Cause your words don't translate
                And it's getting quite late
                So, please don't stay in touch'''
        self.assertTrue(get_mood(l2) < 0.5)
        
suite7 = unittest.defaultTestLoader.loadTestsFromTestCase(TestGetLength)
unittest.TextTestRunner().run(suite7)

class TestGetComplexity(unittest.TestCase): 

    def test1(self):
        l1 = '''Love was when I loved you'''
        self.assertTrue(get_complexity(l1) < 0.5)
        
suite8 = unittest.defaultTestLoader.loadTestsFromTestCase(TestGetLength)
unittest.TextTestRunner().run(suite8)




