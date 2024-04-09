#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const subArr = list.filter((ele) => ele === searchElement);
  return (subArr.length);
};
