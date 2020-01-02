import unittest
from unittest.mock import MagicMock
from . import scraper
from github import GithubException

class getContentsForYaml(unittest.TestCase):

    def createMockContentsFile(self, content, name):
        contentfile_mock = unittest.mock.MagicMock()
        type(contentfile_mock).content = unittest.mock.PropertyMock(return_value=content)
        type(contentfile_mock).name = unittest.mock.PropertyMock(return_value=name)
        return contentfile_mock

    @unittest.mock.patch("github.Repository.Repository")
    def test_github_error(self, mock_class):
        mock_class.get_contents.side_effect = GithubException("", {})
        self.assertEqual([], scraper.getContentsForYaml(mock_class, ""))
        self.assertTrue(mock_class.get_contents.called)

    def test_single_contentfile(self):
        contentfile_mock = unittest.mock.MagicMock()
        type(contentfile_mock).content = unittest.mock.PropertyMock(return_value=1)
        mock = unittest.mock.Mock()
        mock.get_contents.return_value = contentfile_mock
        self.assertEqual([1], scraper.getContentsForYaml(mock, ""))


    def test_array_single_yaml(self):
        mock = unittest.mock.Mock()
        mock.get_contents.return_value = [self.createMockContentsFile(2, "cat.yaml")]
        self.assertEqual([2], scraper.getContentsForYaml(mock, ""))


    def test_array_multiple(self):
        mock = unittest.mock.Mock()
        mock.get_contents.return_value = [
            self.createMockContentsFile(2, "cat.yaml"),
            self.createMockContentsFile(50, "notes.txt"),
            self.createMockContentsFile(4, "cat.yaml"),
            self.createMockContentsFile(100, "cat.yaml")
        ]
        self.assertEqual([2, 4, 100], scraper.getContentsForYaml(mock, ""))


    def test_array_multiple_jenkins(self):
        mock = unittest.mock.Mock()
        mock.get_contents.return_value = [
            self.createMockContentsFile(2, "cat.yml"),
            self.createMockContentsFile(50, "notes.txt"),
            self.createMockContentsFile(4, "cat.yaml"),
            self.createMockContentsFile(100, "JenkinsFile")
        ]
        self.assertEqual([2,4], scraper.getContentsForYaml(mock, ""))


class GetJenkinsConfig(unittest.TestCase):

    def createMockContentsFile(self, content, name):
        contentfile_mock = unittest.mock.MagicMock()
        type(contentfile_mock).content = unittest.mock.PropertyMock(return_value=content)
        type(contentfile_mock).name = unittest.mock.PropertyMock(return_value=name)
        return contentfile_mock

    @unittest.mock.patch("github.Repository.Repository")
    def test_github_error(self, mock_class):
        mock_class.get_contents.side_effect = GithubException("", {})
        self.assertEqual([], scraper.get_jenkins_config(mock_class))
        self.assertTrue(mock_class.get_contents.called)

    def test_array_single_yaml(self):
        mock = unittest.mock.Mock()
        mock.get_contents.return_value = [self.createMockContentsFile(2, "jenkinsfile")]
        self.assertEqual([2], scraper.get_jenkins_config(mock))






if __name__ == '__main__':
    unittest.main()
