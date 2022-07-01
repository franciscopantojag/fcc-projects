const { ObjectId } = require("mongoose").Types;

exports.validateMongoObjectId = (objectId) => ObjectId.isValid(objectId);

exports.validateDate = (date) => {
  const regex = /[0-9]{4}-[0-9]{2}-[0-9]{2}/;
  return regex.test(date);
};
