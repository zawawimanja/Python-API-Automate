import { v4 as uuidv4 } from 'uuid';
import { Router } from 'express';

const router = Router();

const field_required_error = 'This field is required';
const payload_required_error = 'Payload is required';
const message_not_found_error = 'Message not found';

router.get('/', (req, res) => {
  let category = req.query.category;
  if (!category)
    return res.send(req.context.models.messages);
  else{
    return res.send(req.context.models.messages.filter(m => m.category == category));
  }
});

router.get('/:messageId', (req, res) => {

  const messageId = req.params.messageId;

  const messages = req.context.models.messages.filter(m => m.id == messageId);

  if (messages.length == 1)
    return res.status(200).send(messages[0]);
  else {
    return res.status(404).send({message: message_not_found_error});
  }
});

router.post('/', (req, res) => {
  const id = uuidv4();

  const body = req.body;

  console.log(body);
  if(req.body.constructor === Object && Object.keys(req.body).length === 0) {
      res.status(400).send({message: payload_required_error});
  }else{

    const error_response = { errors: {}, message: 'Payload provided doesn\'t meet requirement' };

    let is_error = false;

    if (!body.text){
      error_response.errors.text = field_required_error;
      is_error = true;
    }

    if (!body.category){
      error_response.errors.category = field_required_error;
      is_error = true;
    }

    if (is_error){
      res.status(400).send(error_response);
    }else{

      const message = {
        id,
        text: body.text,
        category: body.category,
      };

      req.context.models.messages.push(message);
      console.log(req.context.models.messages);

      return res.status(200).send(message);
    }
  }
});

router.delete('/:messageId', (req, res) => {

  const messageId = req.params.messageId;

  const messages = req.context.models.messages.filter(m => m.id == messageId);

  if (messages.length == 1){
    req.context.models.messages = req.context.models.messages.filter(m => m.id != messageId);
    return res.status(200).send(messages[0]);
  }else {
    return res.status(404).send({message: message_not_found_error});
  }

});

export default router;
